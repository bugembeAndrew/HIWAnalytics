from django.shortcuts import render
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reports.models import Art, ArtCall

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

def arvs(request):

	querySet = ArtCall.objects.filter(has_arv='No')

	patients = {}
	i = 0
	for patient in querySet:
		item = {i:patient}
		patients.update(item)
		i+=1

	doc = SimpleDocTemplate("arvs.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

	report = []
	name = []
	gender = []
	age = []
	district = []
	tel = []

	# logo = "python_logo.png"
	title = "Patients without ARVS"

	for value in patients.items():
		print(value)
		#name.append(value.name)
		#gender.append(value.gender)
		#age.append(value.age)
		#district.append(value.district)
		#tel.append(value.telephone_number)
	 
	# im = Image(logo, 2*inch, 2*inch)
	# report.append(im)
	 
	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	# ptext = '<font size=12>%s</font>' % formatted_time
	ptext = '<font size=16><b>%s %s %s %s %s</b></font>' % ('Name', 'Gender', 'Age', 'District', 'Telephone Number')
	 
	report.append(Paragraph(ptext, styles["Normal"]))
	report.append(Spacer(1, 12))
	 
	ptext = '<font size=12>%s %s %s %s %s</font>' % (name[0], gender[0], age[0], district[0], tel[0])
	report.append(Paragraph(ptext, styles["Normal"]))       
	
	report.append(Spacer(1, 12))
	doc.build(report)
	
	template = 'reports/arvs.html'
	context = {'doc_dict':doc}
	return render(request, template, context)

def age(request):
	patients = {}
	
	template = 'reports/age.html'
	context = {'art_dict':patients}
	return render(request, template, context)

def challenges(request):
	patients = {}
	
	template = 'reports/challenges.html'
	context = {'art_dict':patients}
	return render(request, template, context)