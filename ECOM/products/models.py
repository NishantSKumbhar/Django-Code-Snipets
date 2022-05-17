import re
from django.db import models


class Discount(models.Model):
    code = models.CharField(max_length=255)
    value = models.IntegerField()
    purpose = models.CharField(max_length=255)

    def __str__(self):
        return self.purpose

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imported = models.CharField(max_length=255)
    discount = models.ForeignKey(Discount,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

    