from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , generics,mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.authtoken.models import Token
from django.forms.models import model_to_dict
from django.db.models import Q
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
import json


class UserData(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUser(APIView):
    permission_classes = (IsAuthenticated,) 
    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserDetails(APIView):
    permission_classes = (IsAuthenticated,) 

    def get_object(self,email_id):
        try:
            return Profile.objects.get(email_id=email_id)
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, email_id, format=None):
        profile = self.get_object(email_id);  
        serializer = ProfileSerializer(profile)
        return Response(serializer.data) 
    
    def put(self, request,email_id, format=None):
        profile = self.get_object(email_id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OtherUserDetails(APIView):
    permission_classes = (IsAuthenticated,) 

    def get_object(self,email_id):
        try:
            return Profile.objects.get(email_id=email_id)
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, email_id, format=None):
        profile = self.get_object(email_id)
        email = request.GET.get('emailId')
        myprofile=self.get_object(email)
        flag=False
        if profile.friends.filter(email_id=email).exists():
            flag=True
        myprofiles=myprofile.friends.all()
        count=myprofile.friends.all().count()
        mutual_count=0
        while count>0:
            if profile.friends.filter(email_id=myprofiles[count-1].email_id).exists():
                mutual_count+=1
            count=count-1
        data = {
            "id":profile.id,
            "name": profile.name,
            "gender": profile.gender,
            "profile pic url": str(profile.profile_pic),
            "permanent address city": str(profile.permanent_address),
            "is person my friend": flag,
            "count of mutual friends":mutual_count
        }
        return Response(data)

class ListOtherUserDetails(APIView):
    permission_classes = (IsAuthenticated,) 

    def get_object(self):
        try:
            return Profile.objects.all()
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        profile = self.get_object()
        email = request.GET.get('emailId')
        gender=request.GET.get('gender',None)
        permanent_address=request.GET.get('city',None)
        myprofile= Profile.objects.get(email_id=email)
        myprofiles=myprofile.friends.all()
        serializer = ProfileSerializer(profile, many=True)
        profile=Profile.objects.all()
        datacount=Profile.objects.all().count()
        finalresult=[]
        while datacount>0:
            if profile[datacount-1].email_id !=email:

                flag=False
                if profile[datacount-1].friends.filter(email_id=email).exists():
                    flag=True
                count=myprofile.friends.all().count()
                mutual_count=0
                while count>0:
                    if profile[datacount-1].friends.filter(email_id=myprofiles[count-1].email_id).exists():
                        mutual_count+=1
                    count=count-1
                address=""
                if profile[datacount-1].permanent_address is not None:
                    address=str(profile[datacount-1].permanent_address.city)
                data = {
                    "id":profile[datacount-1].id,
                    "name": profile[datacount-1].name,
                    "gender": profile[datacount-1].gender,
                    "profile pic url": str(profile[datacount-1].profile_pic),
                    "permanent address city": str(address),
                    "is person my friend": flag,
                    "count of mutual friends":mutual_count
                }
                finalresult.append(data)
            datacount-=1
        if(gender!=None and permanent_address==None):
            finalresult=[x for x in finalresult if x["gender"].lower()==gender.lower()]
        elif  gender==None and permanent_address!=None:
            finalresult=[x for x in finalresult if x["permanent address city"].lower()==permanent_address.lower()]
        elif gender!=None and permanent_address!=None:
            finalresult=[x for x in finalresult if x["permanent address city"].lower()==permanent_address.lower() and x["gender"].lower()==gender.lower()]
        return Response(finalresult)  


class AddFriend(APIView):
    permission_classes = (IsAuthenticated,) 

    def get_object(self,email_id):
        try:
            return Profile.objects.get(email_id=email_id)
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request,email_id, format=None):
        profile=self.get_object(email_id)
        email=request.GET.get('emailId',None)
        if email is None:
            data={
                "Error" :"Invalid Url"
            }
            return Response(data)
        else:
            user_profile=self.get_object(email)
            profile.friends.add(user_profile)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data) 

class RemoveFriend(APIView):
    permission_classes = (IsAuthenticated,) 

    def get_object(self,email_id):
        try:
            return Profile.objects.get(email_id=email_id)
        except Profile.DoesNotExist:
            raise Http404
    
    def get(self, request,email_id, format=None):
        profile=self.get_object(email_id)
        email=request.GET.get('emailId',None)
        if email is None:
            data={
                "Error" :"Invalid Url"
            }
            return Response(data)
        else:
            user_profile=self.get_object(email)
            profile.friends.remove(user_profile)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data) 

            









         

