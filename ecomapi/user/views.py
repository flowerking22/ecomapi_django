from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from .serializers import userserializer,usersignupserializer,useraddressserializer
from .models import usermodel,useraddressmodel
import json
# Create your views here.
@api_view(['GET','POST','DELETE','PUT'])
@csrf_exempt
def user(request):
   if request.method=='PUT':
      try:
            user=usermodel.objects.get(email=request.data['email'])
            serializer=userserializer(user,data=request.data)
            print(request.data)
            if serializer.is_valid():
               serializer.save()
               message={"message":"User updated successfully !!!!"}
               res=JsonResponse(message,status=status.HTTP_200_OK)
               return res
            else:
                print(serializer.errors)
                res=JsonResponse({"serializer error":request.data,"error":serializer.errors},safe=False,status=status.HTTP_404_NOT_FOUND)
      #res.status_code=400
                return res
      except:
         message={"No user Address found this email is ":request.data['email'],"method":"PUT REQUEST OCCUR"}
         return JsonResponse(message,safe=False,status=status.HTTP_304_NOT_MODIFIED)
      res=JsonResponse({"No user Address found":email},safe=False,status=status.HTTP_404_NOT_FOUND)
      #res.status_code=400
      return res
   if request.method=='DELETE':
      try:
         user=usermodel.objects.get(email=request.data['email'])
         user.delete()
         return JsonResponse("user Deleted Successfully",safe=False,status=status.HTTP_200_OK)
      except:
         return JsonResponse("user Deletion Failed",safe=False,status=status.HTTP_304_NOT_MODIFIED)
   #print(request.data)
   if request.method=='POST':
      serialzer=usersignupserializer(data=request.data)
      if serialzer.is_valid():
         serialzer.save()
         return JsonResponse(serialzer.data,safe=False)
      res=JsonResponse({"Serializer Failed":request.data,"serializer error":serialzer.errors},safe=False,status=status.HTTP_406_NOT_ACCEPTABLE)
      #res.status_code=400
      return res
   if request.method=='GET':
      user=usermodel.objects.all()
      serialzer=userserializer(user,many=True)
      return JsonResponse(serialzer.data,safe=False)
@api_view(['POST'])
@csrf_exempt
def login(request):
   #print(type(request.data))
   #print(request.data)
   try:
      user=usermodel.objects.get(password=request.data['password'],email=request.data['email'])
      serializer=userserializer(user)
      if len(serializer.data)>0:
      #if serializer.data['username']:
         return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
   #else:
   except:
      res=JsonResponse({"No user found":request.data},safe=False,status=status.HTTP_404_NOT_FOUND)
      #res.status_code=400
      return res
   res=JsonResponse({"No user found":request.data},safe=False,status=status.HTTP_404_NOT_FOUND)
      #res.status_code=400
   return res
   #return JsonResponse(len(serializer.data),safe=False)  
@api_view(['GET','PUT','DELETE'])
def addressuser(request,email):
   if request.method=='GET':
      try:
         print(email)
         useraddress=useraddressmodel.objects.get(email=email)
         serializer=useraddressserializer(useraddress) 
         print(serializer.data)
         return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
      except:
         message={"message":"No address For this Email ?????    "+str(email)}
         return JsonResponse(message,safe=False,status=status.HTTP_304_NOT_MODIFIED)
   if request.method=='PUT':
      try:
            useraddress=useraddressmodel.objects.get(email=email)
            serializer=useraddressserializer(useraddress,data=request.data)
            print(request.data)
            if serializer.is_valid():
               serializer.save()
               message={"message":"address updated successfully !!!!"}
               res=JsonResponse(message,status=status.HTTP_200_OK)
               return res
            else:
                print(serializer.errors)
                res=JsonResponse({"serializer error":email,"error":serializer.errors},safe=False,status=status.HTTP_404_NOT_FOUND)
      #res.status_code=400
                return res
      except:
         message={"No user Address found this email is ":email,"method":"PUT REQUEST OCCUR"}
         return JsonResponse(message,safe=False,status=status.HTTP_304_NOT_MODIFIED)
      res=JsonResponse({"No user Address found":email},safe=False,status=status.HTTP_404_NOT_FOUND)
      #res.status_code=400
      return res
   if request.method=='DELETE':
      try:
         useraddress=useraddressmodel.objects.get(email=email)
         useraddress.delete()
         return JsonResponse("useraddress Deleted Successfully",safe=False,status=status.HTTP_200_OK)
      except:
         return JsonResponse("useraddress Deletion Failed",safe=False,status=status.HTTP_304_NOT_MODIFIED)
@api_view(['GET','POST'])
@csrf_exempt
def address(request):
   if request.method=='GET':
      try:
         #print(email)
         address=useraddressmodel.objects.all()
         serializer=useraddressserializer(address,many=True) 
         return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
      except:
         message={"message":"User Address NOt FOund"}
         return JsonResponse(message,safe=False,status=status.HTTP_304_NOT_MODIFIED)
   if request.method=='POST':
      try:
         serializer=useraddressserializer(data=request.data) 
         if serializer.is_valid():
            serializer.save()
         #print(serializer.data)
            message={"message":"Useraddres added Successfully","data":serializer.data}
            return JsonResponse(message,safe=False,status=status.HTTP_200_OK)
         else:
            message={"message":"Not able to add user address?????","method":serializer.errors}
            print(serializer.errors)
            return JsonResponse(message,safe=False,status=status.HTTP_304_NOT_MODIFIED)
      except:
         message={"message":"Not able to add user address?????","method":serializer.errors}
         print(serializer.errors)
         return JsonResponse(message,safe=False,status=status.HTTP_304_NOT_MODIFIED)
      message={"message":"Not able to add user address?????"}
      #print(serializer.errors)
      return JsonResponse(message,safe=False,status=status.HTTP_304_NOT_MODIFIED)