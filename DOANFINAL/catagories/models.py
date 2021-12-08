from django.db import models
from django.db.models.base import Model


class Product(models.Model):
    pr_id = models.AutoField(primary_key= 'true')
    pr_type = models.CharField(max_length = 50)
    pr_name = models.CharField(max_length = 50)
    pr_image = models.ImageField()
    pr_price = models.FloatField()
    pr_cals = models.IntegerField()
    pr_energy = models.CharField(max_length= 50)

class Exercise(models.Model):
    ex_id = models.AutoField(primary_key= 'true')
    ex_name = models.CharField(max_length=50)
    ex_cals = models.IntegerField()
    ex_img = models.ImageField(upload_to='static/assets/img/ex/', default='static/assets/img/ex/Hiit.png')

class PT(models.Model):
    pt_id = models.AutoField(primary_key='true')
    pt_name = models.CharField(max_length=50)
    pt_sex = models.CharField(max_length=50)
    pt_age = models.IntegerField()
    pt_exp = models.IntegerField()
    pt_price = models.FloatField()

class whey(models.Model):
    whey_id = models.AutoField(primary_key='true')
    whey_name = models.CharField(max_length=50)
    whey_price = models.FloatField()
    whey_img = models.ImageField(upload_to='static/assets/img/whey/', default='static/assets/img/whey/pic1.png')
    
