from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .models import Customer
from .models import Shop
from .models import Dperson
from .serializers import CustomerSerializer
from .serializers import ShopSerializer
from .serializers import DpersonSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
class DpersonView(viewsets.ModelViewSet):
    queryset = Dperson.objects.all()
    serializer_class = DpersonSerializer

    def post(self,request,*args,**kwargs):
        licens = reqest.data['licens']
        Dperson.objects.create(licens=licens)
        return HttpResponse({'message': 'File uploaded'},status=200)

        photo = reqest.data['photo']
        Dperson.objects.create(photo=photo)
        return HttpResponse({'message': 'File uploaded'},status=200)