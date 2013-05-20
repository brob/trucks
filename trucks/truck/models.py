from django.db import models
import datetime
from django import forms
from django.contrib.auth.models import User

class Truck(models.Model):
	"""docstring for Truck"""
	name = models.CharField(max_length=256)
	description = models.TextField(blank=True)
	slug = models.SlugField()
	twitter = models.CharField(max_length=256, blank=True)
	logo = models.ImageField(upload_to="media", blank=True, null=True)

	@models.permalink
	def get_absolute_url(self):
		return ('truck.views.truckDetail', (), {'slug': self.slug,})
		
	def __unicode__(self):
		return u'%s' % (self.name)
			

class Stop(models.Model):
	"""docstring for Stop"""
	truck = models.ForeignKey(Truck)
	
	address = models.CharField(max_length=500, blank=True)
	zip = models.CharField(blank=True, max_length=5)
	city = models.CharField(max_length=500, blank=True)
	state = models.CharField(max_length=500, blank=True)
	geo = models.CharField(blank=True, max_length=200, help_text="Takes lat,long data. Leave blank to auto-fill on save.")
	full_address = models.TextField(blank=True)
	
	
	
	arrival = models.DateTimeField(blank=True, default=datetime.datetime.now)
	departure = models.DateTimeField(blank=True, default=datetime.datetime.now)
	
	def __unicode__(self):
			return u'%s %s' % (self.truck, self.arrival)

	class Meta:
		get_latest_by = "arrival"


class checkin(models.Model):
	truck = models.ForeignKey(Truck)
	geo = models.CharField(blank=True, max_length=200)
	full_address = models.TextField(blank=True, help_text="Reverse location lookup based on Geo")
	user = models.ForeignKey(User)
	datetime = models.DateTimeField(blank=True, default=datetime.datetime.now)


class checkinForm(forms.ModelForm):
	class Meta:
		model = checkin
		fields = ("truck", "geo", "user", "datetime", "full_address",)

	

class Contact(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()
	