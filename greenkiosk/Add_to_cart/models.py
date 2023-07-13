from django.db import models
from inventory.models import Product

class Add_to_cart(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length = 32)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    image = models.ImageField()
    description = models.TextField()
    

