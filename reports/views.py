from django.shortcuts import render
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reports.models import Art, ArtCall
from datetime import date
from django.http import HttpResponse, Http404

# Create your views here.
# Index view
def index(request):
	template = 'reports/index.html'
	page = {
	'title':'Salutation',
	'Salute':'Hello world!',
	}
	context = {'index_text':page}
	return render(request, template, context)

def arvs_report():

	querySet = ArtCall.objects.filter(has_arv='No')

	patients = {}
	i = 0

	for patient in querySet:
		item = {i:patient}
		patients.update(item)
		i+=1

	doc = SimpleDocTemplate("reports/documents/arvs.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

	report = []
	name = []
	gender = []
	area = []
	district = []
	tel = []

	logo = "logo.jpg"

	for value in patients.items():
		name.append(value[1].art.id)
		gender.append(value[1].art.gender)
		area.append(value[1].art.area)
		district.append(value[1].art.district)
		tel.append(value[1].art.telephone_number)
	 
	im = Image(logo)
	report.append(im)
	report.append(Spacer(1, 12))

	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	p = "Patients without ARVs"
	ptext = '<font size=16><b> %s </b></font>' % (p)
	
	report.append(Paragraph(ptext, styles["Normal"]))
	report.append(Spacer(1, 12))
	
	title = ['Patient ID', 'Gender', 'Area of Residence', 'District', 'Telephone Number']
	data = [title]

	for i, value in enumerate(name):
		data.append([value, gender[i], area[i], district[i], tel[i]])

	t = Table(data,style=[('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
     ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
     ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
     ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
		])

	report.append(t)	
	doc.build(report)

def arvs(request):
	arvs_report()

	pdf = open("reports/documents/arvs.pdf", "rb").read()
	return HttpResponse(pdf, content_type="application/pdf")

def get_age(born):
	today = date.today()
	if(born is None):
		return 0
	return today.year - born.year

def age_report():
	querySet = Art.objects.all()

	patients = {}
	i = 0

	for patient in querySet:
		item = {i:patient}
		patients.update(item)
		i+=1

	doc = SimpleDocTemplate("reports/documents/ages.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

	report = []

	one = 0
	two = 0
	three = 0
	four = 0
	five = 0
	six = 0
	seven = 0
	eight = 0
	nine = 0

	logo = "logo.jpg"

	for value in patients.items():
		age = get_age(value[1].age)
		if(not age is None):
			if(age <= 18):
				one += 1
			elif((age > 18) or (age <= 30)):
				two += 1
			elif((age > 30) or (age <= 40)):
				three += 1
			elif((age > 40) or (age <= 50)):
				four += 1
			elif((age > 50) or (age <= 60)):
				five += 1
			elif((age > 60) or (age <= 70)):
				six += 1
			elif((age > 70) or (age <= 80)):
				seven += 1
			elif((age > 80) or (age <= 90)):
				eight += 1
			elif((age > 90) or (age <= 100)):
				nine += 1
	 
	im = Image(logo)
	report.append(im)
	report.append(Spacer(1, 12))

	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	p = "Number of Positive Patients per Age Group"
	ptext = '<font size=16><b> %s </b></font>' % (p)
	
	report.append(Paragraph(ptext, styles["Normal"]))
	report.append(Spacer(1, 12))
	
	title = ['Age Group', 'Number of HIV Positive Patients']
	data = [title]

	data.append(['Below 18', one])
	data.append(['19 to 30', two])
	data.append(['31 to 40', three])
	data.append(['41 to 50', four])
	data.append(['51 to 60', five])
	data.append(['61 to 70', six])
	data.append(['71 to 80', seven])
	data.append(['81 to 90', eight])
	data.append(['91 to 100', nine])

	t = Table(data,style=[('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
     ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
     ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
     ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
		])

	report.append(t)	
	doc.build(report)

def age(request):
	age_report()

	pdf = open("reports/documents/ages.pdf", "rb").read()
	return HttpResponse(pdf, content_type="application/pdf")

def challenges_report():
	querySet = ArtCall.objects.all()

	patients = {}
	i = 0

	for patient in querySet:
		item = {i:patient}
		patients.update(item)
		i+=1

	doc = SimpleDocTemplate("reports/documents/challenges.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

	report = []
	facility = []
	other = []

	logo = "logo.jpg"

	for value in patients.items():
		if(not value[1].hf_challenges is None):
			facility.append(value[1].hf_challenges)
		if(not value[1].challenges_other is None):
			other.append(value[1].challenges_other)
	 
	im = Image(logo)
	report.append(im)
	report.append(Spacer(1, 12))

	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	p = "Common Challenges faced During ART"
	ptext = '<font size=16><b> %s </b></font>' % (p)
	
	report.append(Paragraph(ptext, styles["Normal"]))
	report.append(Spacer(1, 12))
	
	titleOne = ['Health Facility Challenges']
	data = [titleOne]

	for i, value in enumerate(facility):
		data.append([value])

	titleTwo = ['Personal Challenges']
	data.append(titleTwo)

	for i, value in enumerate(other):
		data.append([value])

	t = Table(data,style=[('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
     ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
     ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
     ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
		])

	report.append(t)	
	doc.build(report)

def challenges(request):
	challenges_report()

	pdf = open("reports/documents/challenges.pdf", "rb").read()
	return HttpResponse(pdf, content_type="application/pdf")