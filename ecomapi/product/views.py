from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import productmodel
from .serializers import productserializer,productupdateserializer
# Create your views here.
def login(request):
    return HttpResponse("Hai")
@api_view(['GET','POST'])
@csrf_exempt
def getall(request):
    try:
        product=productmodel.objects.all()
        serializer=productserializer(product,many=True)
        return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
    except:
        return JsonResponse("Response Failed",safe=False,status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def getone(request,name):
    if request.method=='PUT':
        #return JsonResponse(request.data,safe=False)
        try:
            product=productmodel.objects.get(name=name)
            serializer=productupdateserializer(product,data=request.data)
            print(request.data)
            if serializer.is_valid():
               serializer.save()
               message={"message":"Product updated successfully !!!!"}
               res=JsonResponse(message,status=status.HTTP_200_OK,safe=False)
               return res
        except:
            print(serializer.errors)
            return JsonResponse(serializer.errors,safe=False,status=status.HTTP_304_NOT_MODIFIED)
        print(serializer.errors)
        return JsonResponse(serializer.errors,safe=False,status=status.HTTP_304_NOT_MODIFIED)
    if request.method=='GET':
        try:
            product=productmodel.objects.get(name=name)
            serializer=productserializer(product)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        except:
            message={"message":"No product have this id","method":"PUT REQUEST OCCUR"}
            return JsonResponse(message,safe=False,status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        try:
            product=productmodel.objects.get(name=name)
            serializer=productserializer(product)
            product.delete()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        except:
            return JsonResponse(status=status.HTTP_404_NOT_FOUND,safe=False)
@api_view(['POST'])
@csrf_exempt
def create(request):
    try:
        serializer=productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            message={"data":serializer.data,"status":"Failed"}
            return JsonResponse(message,safe=False,status=status.HTTP_400_BAD_REQUEST)
    except:
        return JsonResponse(status=status.HTTP_510_NOT_EXTENDED)