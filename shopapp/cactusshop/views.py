from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):

    categories = Category.objects.all()
    

    return render(request, 'index.html',{
        'categories':categories,
        


    
    })

def base(request):

    categories = Category.objects.all()
    

    return render(request, 'base.html',{
        'categories':categories,
        


    
    })

   
    
    
