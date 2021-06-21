from django.contrib import admin
from .models import Category, ProductRecommend, PostImage, Contact, Comment
from django.utils.html import format_html

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_description', 'category_status','show_image'] #'category_image'
    list_filter = ['category_name','category_status']
    search_fields = ['category_name']

    # fieldsets = (
    #     (None, {
    #         "fields": ['category_name','show_image', 'category_description ', 'category_status',]}), 
               
    # )

class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 2



@admin.register(ProductRecommend)
class ProductRecommendAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_category','product_price','product_description','product_recommend' ,'product_status', 'images', 'product_updated']
    inlines = [PostImageAdmin]
    search_fields = ['product_name']
    list_filter = ['product_category','product_status']

    def images(self, obj):
        abc = PostImage.objects.filter(post=obj)
        img = '<div>'
        for a in abc:
            img+='<img src="%s" height="100px"> <br/>' % a.images.url
        img+='</div>'
        return format_html(img)
        # return abc.values_list('images',flat=True)
 
    class Meta:
       model = ProductRecommend

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['show_image_product']





    



# class ProductRecommendAdmin(admin.ModelAdmin):
#     
#     #inlines = [PostImageAdmin]

class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','e_mail','message']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['product_comment','message','rating']



    

admin.site.register(Category ,CategoryAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Comment,CommentAdmin)


