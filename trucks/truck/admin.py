from django.contrib import admin
from truck.models import *


class TruckAdmin(admin.ModelAdmin):
	list_display = ('name','slug')
	prepopulated_fields = {"slug": ("name",)}

class StopAdmin(admin.ModelAdmin):
	list_display = ('truck', 'arrival')
	

	
admin.site.register(Truck, TruckAdmin)
admin.site.register(Stop, StopAdmin)