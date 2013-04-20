from django.contrib import admin
from truck.models import *
from truck.views import getZip
from geopy import geocoders


class TruckAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	prepopulated_fields = {"slug": ("name",)}

class StopAdmin(admin.ModelAdmin):
	list_display = ('truck', 'arrival')
	
	def save_model(self, request, obj, form, change):
		if not obj.geo:
			address = (obj.address + " in " + obj.city + " " + obj.state)
			g = geocoders.GoogleV3()
			place, (lat, lng) = g.geocode(address)
			geo = "%.5f, %.5f" % (lat, lng)
			
			obj.geo = geo
			
		

		obj.save()
		if not obj.full_address:
			fullAddress = getZip(obj.geo)
			obj.full_address = fullAddress
		obj.save()
			
				
admin.site.register(Truck, TruckAdmin)
admin.site.register(Stop, StopAdmin)