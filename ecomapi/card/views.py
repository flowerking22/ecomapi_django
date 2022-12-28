from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from .models import cardmodel
from .serializers import cardserializer

# Create your views here.
@api_view(['GET','POST'])
@csrf_exempt
def index(request):
    if request.method=='POST':
        try:
            serializer=cardserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data,safe=False,status=status.HTTP_201_CREATED)
        except:
            pass
        message={"message":"Cart Insert Failed","errors":serializer.errors}
        return JsonResponse(message,safe=False,status=status.HTTP_400_BAD_REQUEST)
    try:
        card=cardmodel.objects.all()
        serializer=cardserializer(card,many=True)
        return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
    except:
       return HttpResponse("<h1>Card Page mOpen</h1>",status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
@csrf_exempt
def getone(request,email):
    try:
        card=cardmodel.objects.all().filter(email=email)
        serializer=cardserializer(card,many=True)
        print(serializer.data)
        print(len(serializer.data))
        if len(serializer.data)>0:
            return JsonResponse(serializer.data,safe=False,status=status.HTTP_200_OK)
        resdata="<h1>card for this user id not found</h1>"+str(id)
        return HttpResponse(resdata,status=status.HTTP_204_NO_CONTENT)
    except:
        resdata="<h1>card is not found</h1>"+str(id)
        return HttpResponse(resdata,status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def modifyone(request,email,name):
        if request.method=='GET':
            try:
                card=cardmodel.objects.get(email=email,productname=name)
                serializer=cardserializer(card)
                #if serializer.is_valid():
                res=JsonResponse(serializer.data,status=status.HTTP_202_ACCEPTED,safe=False)
                return res
            except:
                #print(serializer.errors)
                #message={"serializers.error":serializer.errors}
                #return JsonResponse(message,safe=False,status=status.is_server_error)
                message={"message":"No item for this card and item","serializers.error":"serializer.errors"}
                return JsonResponse(message,safe=False,status=status.HTTP_204_NO_CONTENT)
      
        if request.method=='PUT':
            try:
                card=cardmodel.objects.get(email=email,productname=name)
                serializer=cardserializer(card,data=request.data)
                print(request.data)
                if serializer.is_valid():
                    serializer.save()
                    message={"message":"Card updated successfully !!!!"}
                    res=JsonResponse(message,status=status.HTTP_205_RESET_CONTENT,safe=False)
                    return res
            except:
                print(serializer.errors)
            return JsonResponse(serializer.errors,safe=False,status=status.HTTP_304_NOT_MODIFIED)
        if request.method=='DELETE':
            try:
                card=cardmodel.objects.get(email=email,productname=name)
                card.delete()
                message={"message":"Card Item Deleted successfully !!!!"}
                res=JsonResponse(message,status=status.HTTP_301_MOVED_PERMANENTLY,safe=False)
                return res
            except:
                message={"message":"Card Item Deleted Failed ?????"}
            return JsonResponse(message,safe=False,status=status.HTTP_400_BAD_REQUEST)
        