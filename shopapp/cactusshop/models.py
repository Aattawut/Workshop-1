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
        if self.image:
            return format_html('<img src="' + self.category_image.url + '" height="100px">')
        return ''
    show_image.allow_tags = True