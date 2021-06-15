from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Category, PostImage, ProductRecommend
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    image_list = {}
    products = ProductRecommend.objects.all()
    categories = Category.objects.all()

    for product in products:
        postimage = PostImage.objects.filter(post=product).first()
        image_list[product.id] = postimage.images.url

    return render(request, 'index.html',{
        'categories':categories,
        'products':products,
        'image_list': image_list
    
    })

# def base(request):

#     categories = Category.objects.all()
#     return render(request, 'base.html',{
#         'categories':categories,
           
#     })

# def product_view(request):
    
#     print(products)
    
#     return render(request, 'index.html',{
        
#     })

def contact(request):
    return render(request, 'contact.html')

def category(request):
    return render(request, 'category.html')

# def detail_view(request, id):
#     post = get_object_or_404(ProductRecommend, id=id)
#     photos = PostImage.objects.filter(post=post)
#     return render(request, 'detail.html', {
#         'post':post,
#         'photos':photos,
#     })


   
    
    
