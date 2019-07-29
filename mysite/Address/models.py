from django.db import models

# Create your models here.

class Address(models.Model):
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.IntegerField()
    country=models.CharField(max_length=50)
