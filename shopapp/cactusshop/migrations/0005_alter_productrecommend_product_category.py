# Generated by Django 3.2.4 on 2021-06-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cactusshop', '0004_rename_description_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrecommend',
            name='product_category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products_count', to='cactusshop.category'),
        ),
    ]