from django.db import models
import datetime


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
	
	arrival = models.DateTimeField(blank=True, default=datetime.datetime.now)
	departure = models.DateTimeField(blank=True, default=datetime.datetime.now)
	
	def __unicode__(self):
			return u'%s %s' % (self.truck, self.arrival)
