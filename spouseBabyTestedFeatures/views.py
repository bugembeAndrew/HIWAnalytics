from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import MySQLdb as sql 
import pandas as pd 
from rest_pandas import PandasSimpleView
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from optparse import make_option
from django.core.management.base import BaseCommand
import time 
import datetime
import django
from django.views.generic import CreateView 
from .models import SendSms
from .models import Art
from .models import ArtCall
from .forms import SendSMSForm
from django import forms 
from .utils import send_twilio_message
import twilio
import twilio.rest 
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
	return render(request, 'spouseBabyTestedFeatures/home.html')

#show baby analytical graphs 
def baby_analytical_graphs(request):
	
	return render (request, 'spouseBabyTestedFeatures/baby_graphs.html')

#show spouse analytical graphs
def spouse_analytical_graphs(request):
	
	return render (request, 'spouseBabyTestedFeatures/spouse_graphs.html')

#display details for patients whose babies are not tested
def spouse_not_tested(request):
	mysql_connect = sql.connect( host = '127.0.0.1', port = 3306 , user = 'patient', passwd = 'Patient', db = 'cdr')
	with mysql_connect:
		cur = mysql_connect.cursor()
		cur.execute("select art.id, art.name, art.telephone_number, art_call.spouse_tested from art left join art_call on art.id = art_call.art where spouse_tested = 'No'")
		rows = cur.fetchall()
		for row in rows: 
			spouse_not_tested_records = print (row[0], row[1], row[2], row[3])

		connection.close()
	return render(request, 'spouseBabyTestedFeatures/spouse_not_tested_records.html', {'rows' : rows})

#display details for patients whose babies are not tested
def baby_not_tested(request):
	mysql_connect = sql.connect( host = '127.0.0.1', port = 3306 , user = 'patient', passwd = 'Patient', db = 'cdr')
	with mysql_connect:
		cur = mysql_connect.cursor()
		cur.execute("select art.id, art.name, art.telephone_number, art_call.baby_tested from art left join art_call on art.id = art_call.art where baby_tested = 'No'")
		rows = cur.fetchall()
		for row in rows: 
			baby_not_tested_records = print (row[0], row[1], row[2], row[3])

		connection.close()
	return render(request, 'spouseBabyTestedFeatures/baby_not_tested_records.html', {'rows' : rows})

#display details of sent messages
def view_sent_recommendations(request):
	mysql_connect = sql.connect( host = '127.0.0.1', port = 3306 , user = 'patient', passwd = 'Patient', db = 'cdr')
	with mysql_connect:
		cur = mysql_connect.cursor()
		cur.execute("select to_number, body from send_sms")
		rows = cur.fetchall()
		for row in rows: 
			view_sent_recommendations = print (row[0], row[1])

		connection.close()
	return render(request, 'spouseBabyTestedFeatures/sent_recommendations_records.html', {'rows' : rows})

#send recommendation message to patient 
class SendSmsCreateView(CreateView):
	model = SendSms
	form_class = SendSMSForm
	template_name = 'spouseBabyTestedFeatures/recommendations.html'
	success_url = '/message_sent_successfully/'
	

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

		return super(SendSmsCreateView, self).form_valid(form)

#return on successfully sending a message
def message_sent_successfully(request):
	return render(request, 'spouseBabyTestedFeatures/message_sent.html')		



