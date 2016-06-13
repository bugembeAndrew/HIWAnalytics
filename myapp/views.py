from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from myapp.models import Art
from myapp.models import ArtCall
from django.shortcuts import render_to_response
import random
import datetime
from datetime import date
import time

# Create your views here.
def patientList(request):
	patients = ArtCall.objects.filter(spouse_tested="No").all()
	return render(request,'notestedPatients.html', locals())


def create_linechart(request):
	
	patient_all = Art.objects.all()
	age = 0
	child =0
	youth = 0
	adult = 0
	total = 0

	for patient in patient_all:
		if (not patient.age is  None):
			age =  (date.today() - patient.age).days
			if(age < 6570):
				child +=1
			elif(age > 6570 or age <= 12775):
				youth+=1
			elif(age > 12775):
				adult+=1


	xdata = ["Below 18", "Below 35", "Above 35"]
	ydata = [child, youth, -adult]

	extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
	chartdata = {
    	'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
	}
	charttype = "discreteBarChart"
	chartcontainer = 'discretebarchart_container'  # container name
	data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
		},
	}
	return render(request,'linechart.html',data)
def piechart(request):
	
	male_set = Art.objects.filter(gender="Male").count()
	female_set = Art.objects.filter(gender="Female").count()
	total = male_set + female_set
	#male_set = int((male_set/total)*100)
	#female_set = int((female_set/total)*100)
	xdata = ["Male: " +str(male_set)+"", "Female: "+str(female_set)+""]
	ydata = [male_set, female_set]
	chartdata = {'x': xdata, 'y': ydata}
	charttype = "pieChart"
	chartcontainer = 'piechart_container'
	labelType = "key"
	data = {
		'charttype': charttype,
    	'chartdata': chartdata,
    	'chartcontainer': chartcontainer,
    	'labelType' : labelType,
    	'showLabels' : False,
    	'extra': {
        'x_is_date': False,
        'x_axis_format': '',
        'tag_script_js': True,
        'jquery_on_ready': False,
        }
    }
	return render(request,'piechart.html',data)

def piechartTest(request):
	patients = ArtCall.objects.filter(spouse_tested="No").all()
	all_patients = ArtCall.objects.all()
	total = 0
	yes_set = 0
	no_set = 0
	other = 0
	ven = venn()

	for patient in all_patients:
		if(patient.spouse_tested == "Yes"):
			yes_set+=1
		elif(patient.spouse_tested == "No"):
			no_set+=1
		else:
			other+=1
	total = (yes_set+no_set+other)
	#yes_set = int((yes_set/total)*100)
	#no_set =int((no_set/total)*100)
	#other = int((other/total)*100)

	xdata = ["Spouse Tested: "+str(yes_set)+"", "Not Tested: "+str(no_set)+"","Singles: "+str(other)+""]
	ydata = [yes_set, no_set,other]
	chartdata = {'x': xdata, 'y': ydata}
	charttype = "pieChart"
	chartcontainer = 'piechart_container'
	x_is_date = False
	x_axis_format = ''
	tag_script_js = True
	jquery_on_ready = False
	labelType=    "percent"
	showLabels = True
	donut = True
	return render(request,'piechart2.html',locals())

def piechartBaby(request):
	patients = ArtCall.objects.filter(baby_tested="No").all()
	all_objects = ArtCall.objects.all()
	yes_set = 0
	no_set = 0	
	other = 0 
	total = 0
	baby = femaleBabies()

	for patient in all_objects:
		if(patient.baby_tested == "Yes"):
			yes_set+=1
		elif(patient.baby_tested == "No"):
			no_set+=1
		else:
			other+=1
	total = (yes_set+no_set+other)
	#yes_set =int((yes_set/total)*100)
	#no_set = int((no_set/total)*100)
	#other = int((other/total)*100)

	xdata = ["Baby Tested: "+ str(yes_set)+"", "Not Tested: "+str(no_set) +"","Patients without babies: "+str(other)+""]
	ydata = [yes_set, no_set,other]
	chartdata = {'x': xdata, 'y': ydata}
	charttype = "pieChart"
	chartcontainer = 'piechart_container'
	x_is_date = False
	x_axis_format = ''
	tag_script_js = True
	jquery_on_ready = False
	labelType=    "percent"
	showLabels = True
	donut = True

	return render(request,'piechartBaby.html',locals())

def helpPage(request):

	return render(request,'help.html', locals())

def venn():

	female_set = Art.objects.filter(gender="Female").count()
	patients = ArtCall.objects.filter(spouse_tested="No").all()

	count = 0

	for x in patients:
		if(x.art.gender == 'Female'):
			count += 1

	female_string = 'Of the'+str(female_set)+'Females with HIV'
	string2 ='Only 2 have spouse tested'
	context = {
	'item':{
        'val1':female_set,
        'val2':female_string,
        'val3':string2,
        'val4':patients,
        'val5':str(count),
        }
    }
	return context
	#return render(request,'piechart2.html', context)

def femaleBabies():
	female_set = Art.objects.filter(gender="Female").count()
	patients = ArtCall.objects.filter(baby_tested="No").all()

	count = 0

	for x in patients:
		if(x.art.gender == 'Female'):
			count += 1

	female_string = 'Of the '+str(female_set)+' Males with HIV'
	
	context = {
	'item':{
        'val1':female_set,
        'val2':female_string,
        'val4':patients,
        'val5':str(count),
        }
    }
	return context