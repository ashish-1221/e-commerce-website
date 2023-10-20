from rest_framework import serializers
from .models import Product,ProductCategory,Vendor,Customer,Order,OrderItems
from dataclasses import fields

# Product Model Serializers
class ProductSerializer(serializers.ModelSerializer):
    pass

# Vendor Model Serializer
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
        #self.Meta.depth = 1
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

        #self.Meta.depth = 1

# Product Category Serializer
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','category','vendor','title','detail','price')
    def __init__(self,*args,**kwargs):
        super(ProductListSerializer,self).__init__(*args,**kwargs)
        # self.Meta.depth = 1


## ProductDetailSerializer
class ProductDetailSerializer(serializers.ModelSerializer ):
    class Meta:
        model = Product
        fields = (
            'id',
            'user',
            'address'
        )
    def __init__(self,*args,**kwargs):
        super(ProductDetailSerializer,self).__init__(*args,**kwargs)
        #self.Meta.depth = 1
        

# Vendor Model Serializer
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