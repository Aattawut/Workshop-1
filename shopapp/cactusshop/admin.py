from django.contrib import admin
from .models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_description', 'category_status', 'category_image',]
    list_filter = ['category_name','category_status']
    search_fields = ['category_name']

    # fieldsets = (
    #     (None, {
    #         "fields": ['category_name','show_image', 'category_description ', 'category_status',]}), 
               
    # )
    

admin.site.register(Category ,CategoryAdmin)

