from django.shortcuts import render
from .serializers import VendorSerializer,VendorDetailSerializer,ProductListSerializer, ProductDetailSerializer,CustomerSerializer,CustomerDetailSerializer,OrderSerializer,OrderDetailSerializer
from .models import Vendor,Product,Customer,Order,OrderItems
from rest_framework import generics,permissions,pagination
# Create your views here.

class VendorList(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorDetailSerializer
   

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = pagination.LimitOffsetPagination


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    
    
## Customer 
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

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