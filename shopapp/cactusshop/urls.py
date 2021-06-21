from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    
    url('home/', views.index, name='index'),
    # url('home/', views.product_view, name='product-list'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name='category'),
    path('search/', views.base, name='search'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

]
