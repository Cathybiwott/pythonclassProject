from django.db import models

class Delivery(models.Model):
    name = models.CharField(max_length = 32)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    image = models.ImageField()
    description = models.TextField()
    address = models. CharField(max_length = 33)