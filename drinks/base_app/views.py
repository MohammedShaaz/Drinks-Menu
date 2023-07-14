from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Drinks
from .serializers import DrinkSerializer
# Create your views here.


class DrinksApi(APIView):
    def get(self,request):
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks,many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.error,status= status.HTTP_400_BAD_REQUEST)
    
class DrinksDetails(APIView):

    def get_drink(self,id):
        try :
            return Drinks.objects.get(id = id)
        except Drinks.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        drink = self.get_drink(id)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    
    def put(self,request,id):
        drink = self.get_drink(id)
        serializer = DrinkSerializer(drink,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        drink = self.get_drink(id)
        drink.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
