from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics,permissions,pagination,viewsets
# Create your views here.

## List serializer for vendor
class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

## Detail serializer for Vendor
class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
   
## List Serializer for Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = pagination.LimitOffsetPagination

## Detail Serializer for Product
class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    
    
## Customer List Serializer
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

## Customer Detaul
class CustomerDetail(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerDetailSerializer
    
## Order View Class
class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class =   OrderSerializer

## Order Detail Class
class OrderDetail(generics.ListAPIView):
    #queryset = OrderItems.objects.all()
    serializer_class = OrderDetailSerializer
    
    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        order_items = OrderItems.objects.filter(order=order)
        return order_items


## Create a view according to viewset
class CustomerAddressViewset(viewsets.ModelViewSet):
    serializer_class = CustomerAddressSerializer
    queryset = CustomerAddress.objects.all()

## ProductRating viewset
class ProductRatingViewset(viewsets.ModelViewSet):
    serializer_class = ProductRatingSerializer
    queryset = ProductRating.objects.all()