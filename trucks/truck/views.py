from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from truck.models import *
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.template import defaultfilters
import requests, json
from django.contrib.auth.decorators import login_required

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
		
	checkins = truck.checkin_set.all

	return render_to_response("trucks/truck_detail.html", {
		"test" : "Something",
		'truck' : truck,
		'stop' : stop,
		'checkins' : checkins,
    }, context_instance=RequestContext(request))


def getZip(latlng):
	# grab some lat/long coords from wherever. For this example,
	# I just opened a javascript console in the browser and ran:
	#
	# navigator.geolocation.getCurrentPosition(function(p) {
	# console.log(p);
	# })
	#
	latLngVar = defaultfilters.cut(latlng, " ")

	# Did the geocoding request comes from a device with a
	# location sensor? Must be either true or false.
	sensor = 'true'

	# Hit Google's reverse geocoder directly
	# NOTE: I *think* their terms state that you're supposed to
	# use google maps if you use their api for anything.
	base = "http://maps.googleapis.com/maps/api/geocode/json?"
	params = "latlng={latlng}&sensor={sen}".format(
		latlng = latLngVar,
		sen = "true"
	)
	url = "{base}{params}".format(base=base, params=params)
	response = requests.get(url)
	jsonObj = json.loads(response.content)
	fullAddress = jsonObj['results'][0]['formatted_address']
	return str(fullAddress)



@login_required
def checkin(request):
	"""docstring for checkin"""
	

	if request.method == 'POST':
		c = {}
		c.update(csrf(request))
		form = checkinForm(request.POST)
		if form.is_valid():
			form.save()
			test = "Success"
		return HttpResponseRedirect('/accounts/profile/')
		
	else:
		c = {}
		data = {}
		c.update(csrf(request))
		currentTruck, geo, fullAddress = "", "", ""
		query = request.GET
		if query:		
			user = request.user
			currentTruck = request.GET.get("truck","")
			geo = request.GET.get("lat","") + ", " + request.GET.get("lng","")
			
			if not (currentTruck == ""):
				data['truck'] = Truck.objects.get(name = currentTruck)		
			if not (geo == ", "):
				data['geo'] = geo 
				fullAddress = getZip(geo)
				data['full_address'] = fullAddress
			data['user'] = user
			
		form = checkinForm(initial=data)

		return render_to_response("checkin.html", {
			"truck": currentTruck,
			"geo": geo,
			"form": form,
			'c': c
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
	
def authProfile(request):
	return render (request, 'user/profile.html', {
		'context': 'Context!',
	})