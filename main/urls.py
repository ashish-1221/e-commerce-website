from django.urls import path,include
from .views import *
urlpatterns = [
    path('vendors',VendorList.as_view(),name="vendorlist"),
    path('vendors/<int:pk>',VendorDetail.as_view(),name="vendordetail"),
    path('products/',ProductList.as_view()),
    path('products/<int:pk>',ProductList.as_view()),
    path('customers/',CustomerList.as_view()),
    path('customer/<int:pk>/',CustomerDetail.as_view()),
    ## Orders
    path('orders/',OrderList.as_view()),
    path('order/<int:pk>/',OrderDetail.as_view()),
]