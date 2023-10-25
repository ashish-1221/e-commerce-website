from rest_framework import serializers
from .models import *
from dataclasses import fields



## Vendor Model Serializer
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            'id',
            'user',
            'address'
        )
    
    def __init__(self,*args,**kwargs):
        super(VendorSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

## Vendor Detail Serializer
class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = (
            'id',
            'user',
            'address'
        )
    def __init__(self,*args,**kwargs):
        super(VendorDetailSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

## Product Category Serializer
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','category','vendor','title','detail','price')
    def __init__(self,*args,**kwargs):
        super(ProductListSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1


## ProductDetailSerializer
class ProductDetailSerializer(serializers.ModelSerializer ):
    rating_products = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ('id','category','vendor','title','detail','price','rating_products')
    def __init__(self,*args,**kwargs):
        super(ProductDetailSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1
        

## Customer Model Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'user',
            'mobile',
        )
    
    def __init__(self,*args,**kwargs):
        super(CustomerSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

## Vendor Detail Serializer
class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'user',
            'mobile'
        )
    def __init__(self,*args,**kwargs):
        super(CustomerDetailSerializer,self).__init__(*args,**kwargs)

        self.Meta.depth = 1
        

## Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'customer',
        )
    
    def __init__(self,*args,**kwargs):
        super(OrderSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

## OrderDetail Serializer
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = (
            'id',
            'order',
            'product'
        )
    def __init__(self,*args,**kwargs):
        super(OrderDetailSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

## CustomerAddress Serializer
class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = (
            'id',
            'customer',
            'address',
            'default_address'
        )
    def __init__(self,*args,**kwargs):
        super(CustomerAddressSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1

## ProductViewset Serializer
class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating 
        fields = (
            'id',
            'customer',
            'product',
            'rating',
            'reviews',
            'add_time'
        )
    def __init__(self,*args,**kwargs):
        super(ProductRatingSerializer,self).__init__(*args,**kwargs)
        self.Meta.depth = 1