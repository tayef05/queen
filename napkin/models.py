from operator import mod
from turtle import title

from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30,null=False)
    price = models.DecimalField(decimal_places=2,max_digits=3)
    piece = models.PositiveIntegerField(default='30')
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.title
