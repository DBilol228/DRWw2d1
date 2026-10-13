from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
#from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveAPIView

#class ProductList(ListAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
#
#class ProductCreate(CreateAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
#
#class ProductDestroy(DestroyAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
#
#class ProductUpdate(UpdateAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer
#
#class ProductDetail(RetrieveAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductSerializer

# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# 
# class ProductListCreate(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
# 
# class ProductRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

from rest_framework.viewsets import ModelViewSet

class ProductCRUD(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer