from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Tags(models.Model):
    name=models.CharField(max_length=64)

class User(models.Model):
    username=models.CharField(max_length=64,unique=True)
    email=models.EmailField()
    passwd=models.CharField(max_length=500)
    thumb=models.CharField(max_length=200)


class Blogs(models.Model):
    slug=models.CharField(max_length=64,unique=True)
    user=models.ForeignKey(User,related_name="blogs",on_delete=models.CASCADE,null=True)
    thumb=models.CharField(max_length=200)
    title=models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags=models.ManyToManyField(Tags,related_name="blogs")
    content=tinymce_models.HTMLField()

