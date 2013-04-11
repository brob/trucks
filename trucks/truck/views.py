from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from truck.models import *
from django.core.context_processors import csrf
from django.core.mail import send_mail


def home(request):
	"""docstring for home"""
	truck_list = Truck.objects.all()
	current_time = datetime.datetime.now()
	stops = Stop.objects.filter(departure__gt = current_time)
	return render_to_response("home.html", {
		"trucks": truck_list,
		"stops": stops,
	
	}, context_instance=RequestContext(request))

def truckList(request):
	"""docstring for truckList"""
	truck_list = Truck.objects.all()
	
	return render_to_response("trucks/truck_list.html", {
		"test" : "Something",
		"trucks": truck_list,
    }, context_instance=RequestContext(request))

def truckDetail(request, slug):
	"""docstring for truckDetail"""
	slugValue = slug
	truck = Truck.objects.get(slug = slugValue)
	nextStop = truck.stop_set.latest(field_name='arrival')
	departure = nextStop.departure
	current_time = datetime.datetime.now()
	if current_time < departure:
		stop = nextStop
	else:
		stop = None

	return render_to_response("trucks/truck_detail.html", {
		"test" : "Something",
		'truck' : truck,
		'stop' : stop,
    }, context_instance=RequestContext(request))


def contactForm(request):
	if request.method == 'POST':
		c = {}
		c.update(csrf(request))
		form = Contact(request.POST)
		if form.is_valid():
			message = form.cleaned_data['message']
			fromEmail = form.cleaned_data['email']
			send_mail('Email from Truck Form', message, fromEmail,
			    ['bryanlrobinson@gmail.com'], fail_silently=False)
			return HttpResponseRedirect('/thanks/')
			
	else:
		c = {}
		c.update(csrf(request))
		form = Contact()
	return render (request, 'contact.html', {
		'form': form,
		'c': c,
	})