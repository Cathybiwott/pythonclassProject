from django.db import models

class Order(models.Model):
    name = models.CharField(max_length = 32)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    total = models.DecimalField(max_digits = 8, decimal_places = 3)
    image = models.ImageField()
    description = models.TextField()
    