from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    
    url('home/', views.index, name='index'),
    # url('home/', views.product_view, name='product-list'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name='category'),
]
