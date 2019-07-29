from django.contrib import admin
from .models import Address



class AddressAdmin(admin.ModelAdmin):
    list_display=('street_address','city','state','pincode','country')
    list_filter=('city',)

admin.site.register(Address,AddressAdmin)