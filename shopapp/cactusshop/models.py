from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.FileField(upload_to='upload', null=True, blank=True)
    category_description = models.TextField(null=True, blank=True, max_length=255,)
    category_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.category_name

    def show_image(self):
        if self.category_image:
            return format_html('<img src="' + self.category_image.url + '" height="100px">')
        return ''
    show_image.allow_tags = True

class ProductRecommend(models.Model):    
    product_name = models.CharField(max_length=250)
    product_category = models.ForeignKey(Category,default=None,blank=True, null=True, on_delete=models.CASCADE)

    product_description = models.TextField(max_length=255, null=True, blank=True)

    # product_image = models.FileField(blank=True)
    product_price = models.FloatField(default=0)
    product_recommend = models.BooleanField(default=False)
    product_status = models.BooleanField(default=False)
    product_created = models.DateTimeField(auto_now_add=True)
    product_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Product_Recommend'
 
    def __str__(self):
        return str(self.product_name)

    # def show_image_product(self):
    #     if self.product_image:
    #         return format_html('<img src="' + self.product_image.url + '" height="100px">')
    #     return ''
    # show_image_product.allow_tags = True


class PostImage(models.Model):
    post = models.ForeignKey(ProductRecommend, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'products/')
 
    def __str__(self):
        return self.post.product_name

    def show_image_product(self):
        if self.images:
            return format_html('<img src="' + self.images.url + '" height="100px">')
        return ''
    show_image_product.allow_tags = True