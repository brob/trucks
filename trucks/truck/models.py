from django.db import models
import datetime
from django import forms


class Truck(models.Model):
	"""docstring for Truck"""
	name = models.CharField(max_length=256)
	description = models.TextField(blank=True)
	slug = models.SlugField()
	twitter = models.CharField(max_length=256, blank=True)

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
	
	
	
	arrival = models.DateTimeField(blank=True, default=datetime.datetime.now)
	departure = models.DateTimeField(blank=True, default=datetime.datetime.now)
	
	def __unicode__(self):
			return u'%s %s' % (self.truck, self.arrival)

	class Meta:
		get_latest_by = "arrival"

class Contact(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()
	