from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime,time

def hello(request):
	return HttpResponse("Hello world")

def current_time(request):
	now=datetime.datetime.now()
	return render_to_response('current_time.html',{'current_date':now})
