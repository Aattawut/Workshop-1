from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Category, PostImage, ProductRecommend
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
import requests

# Create your views here.

def index(request):
    image_list = {}
    # products = ProductRecommend.objects.all()
    products = ProductRecommend.objects.order_by('product_price')
    # categories = Category.objects.all()
    categories = Category.objects.order_by('category_name')

    for product in products:
        postimage = PostImage.objects.filter(post=product).first()
        image_list[product.id] = postimage.images.url


    product_link = ProductRecommend.objects.filter(product_status=True)

    categ_id_home = request.GET.get('product_categoryid')
    # print(category_nameid)
    if categ_id_home:
        # ถ้ามีค่า 
        product_link = product_link.filter(product_category_id=categ_id_home)

    return render(request, 'index.html',{
        'categories':categories,
        'products':products,
        'image_list': image_list,
        'categ_id_home':categ_id_home,
      })

def category(request):

    category = Category.objects.all()
    image_list_2 = {}
    # products_2 = ProductRecommend.objects.order_by('product_price')
    products_2 = ProductRecommend.objects.filter(product_status=True)

    productt = ProductRecommend.objects.filter(product_status=True)
    productt = ProductRecommend.objects.order_by('product_price')
    
    sort = request.GET.get('sort','low')
    if sort == 'high':
        productt = productt.order_by('-product_price')
        sort_2 = 'ราคามากไปน้อย'
    else:
        productt = productt.order_by('product_price')
        sort_2 = 'ราคาน้อยไปมาก'


    categ_id = request.GET.get('product_categoryid')
    # print(category_nameid)
    if categ_id:
        # ถ้ามีค่า 
        productt = productt.filter(product_category_id=categ_id)


    search = request.GET.get('search','')
    if search != '':
        productt = productt.filter(product_name__icontains=search)
    import sys
    # print('sdfsdf',search,file=sys.stderr)
    
    
    categories = Category.objects.all()

    for p in products_2:
        postimage_2 = PostImage.objects.filter(post=p).first()
        image_list_2[p.id] = postimage_2.images.url

    

    paginator = Paginator(productt, 8)
    page = request.GET.get('page')
    try:
        productt = paginator.page(page)
    except PageNotAnInteger:
        productt = paginator.page(1)
    except EmptyPage:
        productt = paginator.page(paginator.num_pages)
    


    return render(request, 'category.html',{
        'category':category,
        'products_2':products_2,
        'image_list_2': image_list_2,
        'productt':productt,
        # 'page_obj': page_obj,
        'categ_id':categ_id,
        'categories':categories,
        'sort_2':sort_2,
        'search':search,
    })

def base(request):

    categories = Category.objects.all()
    
   

    productt = ProductRecommend.objects.filter(product_status=True)
    categ_id = request.GET.get('product_categoryid')
    if categ_id:
        # ถ้ามีค่า 
        productt = productt.filter(product_category_id=categ_id)
    return render(request, 'base.html',{
        'categories':categories,
        'categ_id_base':categ_id_base,
        'search':search,
           
    })




def detail(request,pk):
    categories = Category.objects.order_by('category_name')
    
    product_detail = ProductRecommend.objects.filter(product_status=True,pk=pk)
    # products_2 = ProductRecommend.objects.order_by('product_price')
    post = get_object_or_404(ProductRecommend, pk=pk)
    imagess = PostImage.objects.filter(post=post)
    
    image_list = {}
    # products = ProductRecommend.objects.all()
    products = ProductRecommend.objects.order_by('product_price')

    for product in products:
        postimage = PostImage.objects.filter(post=product).first()
        image_list[product.id] = postimage.images.url

    categ_id = request.GET.get('product_categoryid')
    # print(category_nameid)
    if categ_id:
        # ถ้ามีค่า 
        productt = productt.filter(product_category_id=categ_id)

    return render(request, 'detail.html',{
        'product_detail':product_detail,
        'imagess':imagess,
        'categories':categories,
        'image_list':image_list,
        'products':products,
        'categ_id':categ_id,
        
    })

def contact(request):
    formcontact = ContactForm()
    categories = Category.objects.all()

    if request.method == 'POST':
        payload = { 'secret':settings.RECAPTCHA_SECRET_TOKEN ,'response':request.POST['g-recaptcha-response']}
        response = requests.post('https://www.google.com/recaptcha/api/siteverify',payload)
        print(response.json()['success'])
        if response.json()['success']:
            formcontact = ContactForm(request.POST)
            if formcontact.is_valid():
                form = formcontact.save(commit=False)
                form.save()
                messages.success(request, 'Save success')
        else:
            messages.error(request, 'Save failed')

        
           
        
        
        formcontact = ContactForm()


    return render(request, 'contact.html',{
        'formcontact':formcontact,
        'categories':categories,
    })

# def detail_view(request, id):
#     post = get_object_or_404(ProductRecommend, id=id)
#     photos = PostImage.objects.filter(post=post)
#     return render(request, 'detail.html', {
#         'post':post,
#         'photos':photos,
#     })


   
    
    
