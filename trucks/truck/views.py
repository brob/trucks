from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from truck.models import *

truck_list = Truck.objects.all()

def home(request):
	"""docstring for home"""
	return render_to_response("home.html", {
		"trucks": truck_list,
	
	}, context_instance=RequestContext(request))

def truckList(request):
	"""docstring for truckList"""
	return render_to_response("trucks/truck_list.html", {
		"test" : "Something",
		"trucks": truck_list,
    }, context_instance=RequestContext(request))

def truckDetail(request, slug):
	"""docstring for truckDetail"""
	slugValue = slug
	truck = Truck.objects.get(slug = slugValue)
	nextStop = truck.stop_set.latest(field_name='arrival')

	return render_to_response("trucks/truck_detail.html", {
		"test" : "Something",
		'truck' : truck,
		'stop' : nextStop,
    }, context_instance=RequestContext(request))