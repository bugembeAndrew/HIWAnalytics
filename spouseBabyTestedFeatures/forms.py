from django.conf import settings 
from django import forms 
from django.forms import ModelForm
from .models import SendSms, Art, ArtCall
from django.forms import TextInput, Textarea

class SendSMSFormSpouse(forms.ModelForm):
	qs = Art.objects.filter(artcall__spouse_tested = 'No',artcall__art__isnull = False).values_list('telephone_number', flat=True).distinct()
	qs_choices = [('', 'Select Phone Number from drop down')] + [(telephone_number, telephone_number) for telephone_number in qs]
	to_number = forms.ChoiceField(qs_choices, required = False)
	body = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 50}))

	class Meta:
		model = SendSms
		fields = ('to_number', 'body')

class SendSMSFormBaby(forms.ModelForm):
	qs = Art.objects.filter(artcall__baby_tested = 'No',artcall__art__isnull = False).values_list('telephone_number', flat=True).distinct()
	qs_choices = [('', 'Select Phone Number from drop down')] + [(telephone_number, telephone_number) for telephone_number in qs]
	to_number = forms.ChoiceField(qs_choices, required = False)
	body = forms.CharField(widget=forms.Textarea(attrs={'rows': 7, 'cols': 50}))

	class Meta:
		model = SendSms
		fields = ('to_number', 'body')

