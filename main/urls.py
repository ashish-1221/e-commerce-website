from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address',CustomerAddressViewset)
router.register('product_rating',ProductRatingViewset)



urlpatterns = [
    ##Vendors
    path('vendors',VendorList.as_view(),name="vendorlist"),
    path('vendors/<int:pk>',VendorDetail.as_view(),name="vendordetail"),
    ##Products
    path('products/',ProductList.as_view()),
    path('products/<int:pk>',ProductDetail.as_view()),
    ##Customers
    path('customers/',CustomerList.as_view()),
    path('customer/<int:pk>/',CustomerDetail.as_view()),
    ## Orders
    path('orders/',OrderList.as_view()),
    path('order/<int:pk>/',OrderDetail.as_view()),
    ## CustomerAddres 
]

urlpatterns+=router.urls