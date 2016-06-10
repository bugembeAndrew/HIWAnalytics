from django.shortcuts import render
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from bayes.models import IncomingCall
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
# Index view
def calls(request):
	template = 'bayes/index.html'
	data = bayes()
	return render(request, template, data)

# classifier
def classifier():
	hiv = 'HIV negative HIV positive'
	hiv2 = 'CD4 count ART'
	hiv3 = 'ARVs arvs virals anti retrovirals'
	hiv4 = 'HIV spread HIV signs'
	hiv5 = 'HIV hiv AIDS HIV/AIDS'

	pregnancy = 'premature ejaculation'
	pregnancy1 = 'pregnant PG expectant'
	pregnancy2 = 'conceive ante natal'
	pregnancy3 = 'birth caesarean c-section'
	pregnancy4 = 'infertility erect fallopian'

	vmmc = 'vmmc VMMC'
	vmmc1 = 'circumcise circumcised circumcision'
	vmmc2 = 'voluntary male medical circumcision'
	vmmc3 = 'safe male circumcision'
	vmmc4 = 'male circumcision'

	sex = 'urinate urinary uti urethra'
	sex1 = 'sex intercourse STDs'
	sex2 = 'vagina genital scrotum testicles penis'
	sex3 = 'candida syphillis gonorrhoea fibroids'
	sex4 = 'foreplay abstain faithful condoms'

	inquiry = 'trying number'
	inquiry1 = 'seek clarification HIWA call centre services'
	inquiry2 = 'know services offer'
	inquiry3 = 'services rendered'
	inquiry4 = 'location Toll free service works'

	train = [
	    (hiv, 'HIV and ART'),
	    (hiv2, 'HIV and ART'),
	    (hiv3, 'HIV and ART'),
	    (hiv4, 'HIV and ART'),
	    (hiv5, 'HIV and ART'),
	    (pregnancy, 'Family Planning, Pregnancy and Infertility'),
	    (pregnancy1, 'Family Planning, Pregnancy and Infertility'),
	    (pregnancy2, 'Family Planning, Pregnancy and Infertility'),
	    (pregnancy3, 'Family Planning, Pregnancy and Infertility'),
	    (pregnancy4, 'Family Planning, Pregnancy and Infertility'),
	    (vmmc, 'Circumcision'),
	    (vmmc1, 'Circumcision'),
	    (vmmc2, 'Circumcision'),
	    (vmmc3, 'Circumcision'),
	    (vmmc4, 'Circumcision'),
	    (sex, 'Sex and STDs'),
	    (sex1, 'Sex and STDs'),
	    (sex2, 'Sex and STDs'),
	    (sex3, 'Sex and STDs'),
	    (sex4, 'Sex and STDs'),
	    (inquiry, 'Service Inquiry'),
	    (inquiry1, 'Service Inquiry'),
	    (inquiry2, 'Service Inquiry'),
	    (inquiry3, 'Service Inquiry'),
	    (inquiry4, 'Service Inquiry')
	]
	test = [
	    
	]

	cl = NaiveBayesClassifier(train)

	return cl

# naive bayes algorithm classification
def bayes():
	all_calls = IncomingCall.objects.all()
	cl = classifier();

	hiv = 0
	pregnancy = 0
	vmmc = 0
	sex = 0
	inquiry = 0

	# Classify reasons
	for call in all_calls:
		if(cl.classify(call.reason_for_call)=='HIV and ART'):
			hiv += 1
		elif(cl.classify(call.reason_for_call)=='Family Planning, Pregnancy and Infertility'):
			pregnancy += 1
		elif(cl.classify(call.reason_for_call)=='Circumcision'):
			vmmc += 1
		elif(cl.classify(call.reason_for_call)=='Sex and STDs'):
			sex += 1
		elif(cl.classify(call.reason_for_call)=='Service Inquiry'):
			inquiry += 1
		else:
			print('Unknown class of data.')
			break
	
	data = {'hiv':hiv, 'other':pregnancy, 'vmmc':vmmc, 'reproductive':sex, 'inquiry':inquiry}
	#template = 'bayes/analytics.html'
	context = {'data_dict':data}
	#return render(request, template, context)
	return context