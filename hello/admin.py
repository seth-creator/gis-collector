from django.contrib import admin

# Register your models here.
#from leaflet.admin import LeafletGeoAdmin

from .models import MonOffre

#class OffreAdmin(LeafletGeoAdmin) :
    #display = ('commune')

#Register your models here.
admin.site.register(MonOffre)