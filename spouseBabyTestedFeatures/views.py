from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic.list import ListView
from optparse import make_option
from django.core.management.base import BaseCommand
import time 
import datetime
import django
from django.views.generic import DetailView
from django.views.generic import CreateView 
from .models import SendSms
from .models import Art
from .models import ArtCall
from .forms import SendSMSFormSpouse, SendSMSFormBaby
from django import forms 
import twilio
import twilio.rest
from .utils import send_twilio_message
import twilio
import twilio.rest 
from django.core.urlresolvers import reverse_lazy

def _send_sms_notification(to, message_body):
	client = twilio.rest.TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
	client.messages.create(to=to,
                           from_= settings.TWILIO_PHONE_NUMBER,
                           body=message_body
                           )

# Create your views here.
def index(request):
	return render(request, 'spouseBabyTestedFeatures/home.html')

#show baby analytical graphs generated outside.
def baby_analytical_graphs(request):
	
	return render (request, 'spouseBabyTestedFeatures/baby_graphs.html')

#show spouse analytical graphs generated outside. 
def spouse_analytical_graphs(request):
	
	return render (request, 'spouseBabyTestedFeatures/spouse_graphs.html')

#display details for patients whose babies are not tested
def spouse_not_tested(request):
	qs = Art.objects.filter(artcall__spouse_tested = 'No', artcall__art__isnull = False).values('id', 'name','telephone_number')
	return render(request, 'spouseBabyTestedFeatures/patient_spouse_not_tested_records.html', {'qs' : qs})


#display details for patients whose babies are not tested
def baby_not_tested(request):
	qs = Art.objects.filter(artcall__baby_tested = 'No', artcall__art__isnull = False).values('id', 'name','telephone_number')
	return render(request, 'spouseBabyTestedFeatures/patient_baby_not_tested_records.html', {'qs' : qs})

	
#display details of sent messages
class RecommendationsListView(ListView):
	model = SendSms
	template_name = 'spouseBabyTestedFeatures/recommendation_list.html'

#send recommendation message to patient whose spouse is not tested 
class SendSmsToPatientWhoseSpouseNotTestedCreateView(CreateView):
	model = SendSms
	form_class = SendSMSFormSpouse
	template_name = 'spouseBabyTestedFeatures/spouserecommendations.html'
	success_url = '/tested/message_sent_successfully/'
	

	def form_valid(self, form):
		number = form.cleaned_data['to_number']
		body = form.cleaned_data['body']
		
		#call twilio
		sent = send_twilio_message(number,body)

		#save form
		send_sms = form.save(commit = False)
		send_sms.from_number = settings.TWILIO_PHONE_NUMBER
		send_sms.sms_sid = sent.sid
		send_sms.account_sid = sent.account_sid
		send_sms.status = sent.status
		send_sms.sent_at = datetime.datetime.now()
		if sent.price:
			send_sms.price = Decimal(force_text(sent.price))
			send.sms.price_unit = sent.price_unit
		send_sms.save()

		return super(SendSmsToPatientWhoseSpouseNotTestedCreateView, self).form_valid(form)

#send recommendation message to patient whose baby is not tested  
class SendSmsToPatientWhoseBabyNotTestedCreateView(CreateView):
	model = SendSms
	form_class = SendSMSFormBaby
	template_name = 'spouseBabyTestedFeatures/babyrecommendations.html'
	success_url = '/tested/message_sent_successfully/'
	

	def form_valid(self, form):
		number = form.cleaned_data['to_number']
		body = form.cleaned_data['body']
		
		#call twilio
		sent = send_twilio_message(number,body)

		#save form
		send_sms = form.save(commit = False)
		send_sms.from_number = settings.TWILIO_PHONE_NUMBER
		send_sms.sms_sid = sent.sid
		send_sms.account_sid = sent.account_sid
		send_sms.status = sent.status
		send_sms.sent_at = datetime.datetime.now()
		if sent.price:
			send_sms.price = Decimal(force_text(sent.price))
			send.sms.price_unit = sent.price_unit
		send_sms.save()

		return super(SendSmsToPatientWhoseBabyNotTestedCreateView, self).form_valid(form)



def message_patients(id):
	qs =  Art.objects.filter(artcall__spouse_tested = 'No',artcall__art__isnull = False).values_list('telephone_number', flat=True).distinct().get(id)
	for q in qs:
		_send_sms_notification(q.telephone_number,
                          'Hello there! This is TMCG. May you please sign up for a couples check up.')
	success_url = '/tested/message_sent_successfully/'


#return on successfully sending a message
def message_sent_successfully(request):
	return render(request, 'spouseBabyTestedFeatures/message_sent.html')
