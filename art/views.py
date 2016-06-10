from django.shortcuts import render
from textblob.classifiers import NaiveBayesClassifier
from art.models import Art, ArtCall, IncomingCall
from django.http import HttpResponse, Http404
from django.template import loader
from datetime import date

# Create your views here.
# Index view
def index(request):
    val1 = piechart()
    val2 = piechartTest()
    val3 = piechartBaby()
    val4 = create_linechart()
    val5 = parents()
    val6 = patientList()

    context = {
    'item':{
        'val1':val1,
        'val2':val2,
        'val3':val3,
        'val4':val4,
        'val5':val5,
        'val6':val6,
        }
    }
    return render(request,'art/index.html', context)

def patientList():
    patients = ArtCall.objects.filter(spouse_tested="No").all()
    return patients

def parents():
    patients = ArtCall.objects.filter(baby_tested="No").all()
    return patients

def create_linechart():  
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
            elif(age >6570 <=12775):
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
    return data

def piechart():
    male_set = Art.objects.filter(gender="Male").count()
    female_set = Art.objects.filter(gender="Female").count()
    total = male_set + female_set
    male_set = int((male_set/total)*100)
    female_set = int((female_set/total)*100)
    xdata = ["Male :" +str(male_set)+"%", "Female :"+str(female_set)+"%"]
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
    return data

def piechartTest():
    patients = ArtCall.objects.filter(spouse_tested="No").all()
    all_patients = ArtCall.objects.all()
    total = 0
    yes_set = 0
    no_set = 0
    other = 0

    for patient in all_patients:
        if(patient.spouse_tested == "Yes"):
            yes_set+=1
        elif(patient.spouse_tested == "No"):
            no_set+=1
        else:
            other+=1
    total = (yes_set+no_set+other)
    yes_set = int((yes_set/total)*100)
    no_set =int((no_set/total)*100)
    other = int((other/total)*100)

    xdata = ["Spouse Tested "+str(yes_set)+"%", "Not Tested "+str(no_set)+"%","N/A "+str(other)+"%"]
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
    return locals()

def piechartBaby():
    patients = ArtCall.objects.filter(baby_tested="No").all()
    all_objects = ArtCall.objects.all()
    yes_set = 0
    no_set = 0  
    other = 0 
    total = 0

    for patient in all_objects:
        if(patient.baby_tested == "Yes"):
            yes_set+=1
        elif(patient.baby_tested == "No"):
            no_set+=1
        else:
            other+=1
    total = (yes_set+no_set+other)
    yes_set =int((yes_set/total)*100)
    no_set = int((no_set/total)*100)
    other = int((other/total)*100)

    xdata = ["Baby Tested :"+ str(yes_set)+"%", "Not Tested :"+str(no_set) +"%","N/A :"+str(other)+"%"]
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
    return locals()