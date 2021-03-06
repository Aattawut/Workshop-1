# Generated by Django 3.2.4 on 2021-06-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cactusshop', '0002_alter_productrecommend_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('e_mail', models.EmailField(max_length=70)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
