from django.db import models
from Address.models import Address
from django.utils.html import format_html


# Create your models here.

gender_choices = (
    ('male','Male'),
    ('female', 'Female'),
    ('other','Other')
)

class Profile(models.Model):
    name=models.CharField(max_length=30)
    email_id=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=16)
    gender=models.CharField(max_length=6,choices=gender_choices,blank=True)
    profile_pic=models.ImageField(upload_to='images\\',blank=True)
    date_of_birth= models.DateField(max_length=8,blank=True,null=True)
    permanent_address=models.OneToOneField(Address,related_name="permanent_address",on_delete=models.CASCADE,blank=True,null=True)
    company_address=models.OneToOneField(Address,related_name="company_address",on_delete=models.CASCADE,blank=True,null=True)
    friends=models.ManyToManyField("Profile",blank=True)

    def user_image(self, obj):
        return format_html('<img src="{}" />'.format(obj.profile_pic.url))
    # def image_tag(self):
    #     from django.utils.html import escape
    #     return u'<img src="%s" />' %escape(self.profile_pic)
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True






