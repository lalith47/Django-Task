from django.contrib import admin
from .models import Profile
from django.utils.html import format_html




class ProfileAdmin(admin.ModelAdmin):
    
    def user_image(self, obj):
        return format_html('<img src="{}" />'.format(obj.profile_pic.url))
    
    search_fields=('name',)
    list_display = ('id','name','gender','date_of_birth' )
    list_filter = ('gender', )
    #fields = ('user_image' )
    # readonly_fields = ('image_tag',)

admin.site.register(Profile,ProfileAdmin)