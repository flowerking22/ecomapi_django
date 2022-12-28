from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ordersmodel
from .serializers import ordersserializer

# Create your views here.
from django.http import HttpResponse
@api_view(['GET','POST'])
@csrf_exempt
def index(request):
    if request.method=='GET':
        order=ordersmodel.objects.all()
        serializer=ordersserializer(order,many=True)
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
    if request.method=='POST':
        serialzer=ordersserializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data,safe=False,status=status.HTTP_200_OK)
        res=JsonResponse({"Serializer Failed":request.data,"serializer error":serialzer.errors},safe=False,status=status.HTTP_406_NOT_ACCEPTABLE)
      #res.status_code=400
        return res
    print(request.data)
    return JsonResponse('Orders,page',safe=False,status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','POST','PUT'])
@csrf_exempt
def getbyproduct(request,id):
    
    # if request.method=='PUT':
    #     #return JsonResponse(request.data,safe=False)
    #     try:
    #         product=ordersmodel.objects.get(userid=id)
    #         serializer=ordersserializer(product,data=request.data)
    #         print(request.data)
    #         if serializer.is_valid():
    #            serializer.save()
    #            message={"message":"Product updated successfully !!!!"}
    #            res=JsonResponse(message,status=status.HTTP_202_ACCEPTED,safe=False)
    #            return res
    #     except:
    #         print(serializer.errors)
    #         return JsonResponse(serializer.errors,safe=False,status=status.HTTP_304_NOT_MODIFIED)
    #     print(serializer.errors)
    #     return JsonResponse(serializer.errors,safe=False,status=status.HTTP_304_NOT_MODIFIED)
    if request.method=='GET':
        try:
            product=ordersmodel.objects.all().filter(productid=id)
            serializer=ordersserializer(product,many=True)
            print(request.data)
            if len(serializer.data)>0:
                return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        except:
            message={"message":"No product have this id","method":"PUT REQUEST OCCUR"}
            return JsonResponse(message,safe=False,status=status.HTTP_404_NOT_FOUND)
    message={"message":"No product have this id"}
    return JsonResponse(message,safe=False,status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST','PUT'])
@csrf_exempt
def getbyuser(request,email):
    # if request.method=='PUT':
    #     #return JsonResponse(request.data,safe=False)
    #     try:
    #         product=ordersmodel.objects.get(userid=id)
    #         serializer=ordersserializer(product,data=request.data)
    #         print(request.data)
    #         if serializer.is_valid():
    #            serializer.save()
    #            message={"message":"Product updated successfully !!!!"}
    #            res=JsonResponse(message,status=status.HTTP_202_ACCEPTED,safe=False)
    #            return res
    #     except:
    #         print(serializer.errors)
    #         return JsonResponse(serializer.errors,safe=False,status=status.HTTP_304_NOT_MODIFIED)
    #     print(serializer.errors)
    #     return JsonResponse(serializer.errors,safe=False,status=status.HTTP_304_NOT_MODIFIED)
    if request.method=='GET':
        try:
            product=ordersmodel.objects.all().filter(email=email)
            serializer=ordersserializer(product,many=True)
            print(request.data)
            if len(serializer.data)==0:
                message={"message":"No order have this Email"}
                return JsonResponse(message,safe=False,status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
        except:
            message={"message":"Error in Server"}
            return JsonResponse(message,safe=False,status=status.HTTP_403_FORBIDDEN)
    message={"message":"No product have this id"}
    return JsonResponse(message,safe=False,status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','DELETE','PUT'])
@csrf_exempt
def getonlyone(request,pid,email):
    if request.method=='GET':
        try:
            print(email,'-',pid)
            order=ordersmodel.objects.all().filter(email=email,productid=pid)
            serializer=ordersserializer(order,many=True)
            #message={"message":"Order Item Deleted successfully !!!!"}
            res=JsonResponse(serializer.data,status=status.HTTP_200_OK,safe=False)
            return res
        except:
            message={"message":"Order Item NOT FOUND ??????"}
            return JsonResponse(message,safe=False,status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        try:
            card=ordersmodel.objects.all().filter(email=email,productid=pid)
            card.delete()
            message={"message":"Order Item Deleted successfully !!!!"}
            res=JsonResponse(message,status=status.HTTP_301_MOVED_PERMANENTLY,safe=False)
            return res
        except:
            message={"message":"Order Item Deleted Failed ??????"}
            return JsonResponse(message,safe=False,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PUT':
        try:
            card=ordersmodel.objects.all().filter(email=email,productid=pid)
            serializer=ordersserializer(card,data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                message={"message":"Order updated successfully !!!!"}
                res=JsonResponse(message,status=status.HTTP_205_RESET_CONTENT,safe=False)
                return res
        
            res=JsonResponse(message,status=status.HTTP_301_MOVED_PERMANENTLY,safe=False)
            return res
        except:
            message={"message":"Order Item Updated Failed ?????"}
            return JsonResponse(message,safe=False,status=status.HTTP_400_BAD_REQUEST)
        