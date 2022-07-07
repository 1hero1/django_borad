from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Borad(models.Model):
    name=models.CharField(max_length=50,unique=True)
    description=models.CharField(max_length=200)
    create_data=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.name

class Topci(models.Model):
    subject=models.CharField(max_length=255)
    borad=models.ForeignKey(Borad,related_name='topics',on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    created_data=models.DateTimeField(auto_now_add=True)

class post(models.Model):
    massage=models.TextField(max_length=4000)
    topic=models.ForeignKey(Topci,related_name='posts',on_delete=models.CASCADE)
    create_by=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_data=models.DateTimeField(auto_now_add=True)
