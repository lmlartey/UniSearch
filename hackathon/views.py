from django.http import HttpResponse, Http404
from django.template.loader import get_template 
from django.template import Context
from django.shortcuts import render_to_response
import datetime,time
from UniSearchApp.models import University, Hostels

def hello(request):
	return HttpResponse("Hello world")

def current_time(request):
	now=datetime.datetime.now()
	return render_to_response('base.html',{'current_date':now})

def selectUniversity(request,id):
	university=University.objects.get(pk=id)
	t=loader.get_template('base.html')
 	c=Context({'university':university})
 
def University_list(request):
	university_list = University.objects.all()
	t = loader.get_template('unversity_list.html')
	c = Context({'university_list': university_list})
 	return HttpResponse(t.render(c))
