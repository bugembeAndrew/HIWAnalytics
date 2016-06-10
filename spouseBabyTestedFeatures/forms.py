from django.conf import settings 
from django import forms 
from django.forms import ModelForm
from .models import SendSms

class SendSMSForm(forms.ModelForm):
	class Meta:
		model = SendSms
		fields = ('to_number', 'body')

