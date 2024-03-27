from django.contrib import admin
from home.models import *


# Register your models here.

class contactadmin(admin.ModelAdmin):
    list_display=['name', 'email', 'msg']

class DonatebloodAdmin(admin.ModelAdmin):
     list_display=['fname', 'email', 'date', 'bloodGroup', 'contactNumber']



class requestAdmin(admin.ModelAdmin):
     list_display=['fullname', 'email', 'quantity','desc', 'bloodGroup', 'contactNumber', 'urgency']

admin.site.register(contact, contactadmin)
admin.site.register(Donateblood, DonatebloodAdmin)
admin.site.register(requestBlood, requestAdmin)