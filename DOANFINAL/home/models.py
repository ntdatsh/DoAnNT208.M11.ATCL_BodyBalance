from django.db import models
from django.db.models.base import Model
from enum import auto
# Create your models here.

# class SanPham(models.Model):
#     name= models.CharField(max_length=100, blank=True, null=True)
#     img= models.ImageField(upload_to='upload')

class Product(models.Model):
    pr_id = models.AutoField(primary_key= 'true')
    pr_type = models.CharField(max_length = 50)
    pr_name = models.CharField(max_length = 50)
    pr_image = models.ImageField()
    pr_price = models.FloatField()
    pr_cals = models.IntegerField()
    pr_energy = models.CharField(max_length= 50)