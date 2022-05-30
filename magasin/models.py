from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=128)
    slug=models.SlugField(max_length=128)
    price=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image=models.ImageField(upload_to="products",blank=True,null=True)
    note=models.IntegerField(default=0.0)
    def __str__(self): 
        return self.name 
