from django.shortcuts import render
from art.models import Art
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.
# Index view
def index(request):
	template = loader.get_template('art/index.html')
	context = {'index_text':'Index Page'}
	return HttpResponse(template.render(context, request))

# List view
from django.views.generic.list import ListView

class ArtListView(ListView):
	model = Art

# CRUD
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class ArtCreate(CreateView):
    model = Art
    fields = ['name', 'gender', 'age', 'district', 'area', 'designation', 
    'sector', 'telephone_number', 'created_at', 'created_by']

class ArtUpdate(UpdateView):
    model = Art
    fields = ['name', 'gender', 'age', 'district', 'area', 'designation', 
    'sector', 'telephone_number', 'created_at', 'created_by']

class ArtDelete(DeleteView):
    model = Art
    success_url = reverse_lazy('patient-list')