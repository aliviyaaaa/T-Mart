from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=20)

class Cashier(models.Model):
    cusername=models.CharField(max_length=30,unique=True)
    cname=models.CharField(max_length=30)
    cdate=models.DateField()
    cemail=models.EmailField(max_length=40)
    cphone=models.CharField(max_length=30)
    caadhar=models.CharField(max_length=30)
    cpassword=models.CharField(max_length=20)

class Category(models.Model):
    name=models.CharField(max_length=30,unique=True)

class Products(models.Model):
    pname = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category_id=models.IntegerField()
    category = models.CharField(max_length=50)

class Loghistory(models.Model):
    data=models.CharField(max_length=100)