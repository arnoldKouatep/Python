from turtle import title
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    