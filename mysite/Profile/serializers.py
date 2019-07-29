from rest_framework import serializers
from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
     model = Profile
     fields = '__all__'
    # class Meta:
    #     model = Profile
    #     fields = ['name', 'email_id', 'phone_number', 'password', 'gender','date_of_birth']