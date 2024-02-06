from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Book(models.Model):
#     book_name = models.CharField(max_length=50,null=True,blank=True)
#     book_author = models.CharField(max_length=50,null=True,blank=True)
#     image = models.ImageField(null=True,blank=True,default='/placeholder.png')

#     createdTime=models.DateTimeField(auto_now_add=True)
#     fields =['book_name','book_author']
 
#     def __str__(self):
#            return f"Book name: {self.book_name}, Book author: {self.book_author}"


class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,blank=True,default='/IMG_0151-new.jpg')
    fields =['desc','price']
 
    def __str__(self):
           return self.desc
