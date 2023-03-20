import datetime

from django.db import models
import os
import datetime

# Create your models here.
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)
    return os.path.join('uploads/',filename)
class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.CharField(max_length=200)
    big_description=models.TextField(max_length=500)
    price=models.FloatField()
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s%s' %(self.category,self.name)