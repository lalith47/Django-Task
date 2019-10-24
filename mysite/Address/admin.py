from django.contrib import admin
from .models import Address



class AddressAdmin(admin.ModelAdmin):
    list_display=('street_address','city','state','pincode','country')
    list_filter=('city',)
    
    def CheckInAddress(name):
        if name in list_display:
            return "valid"
        
admin.site.register(Address,AddressAdmin)
