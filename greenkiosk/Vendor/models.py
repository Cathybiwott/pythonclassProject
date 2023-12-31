from django.db import models



class Vendor(models.Model):
    name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 33)
    image = models.ImageField()
    phone_number = models.CharField(max_length = 10)
    date_created = models.DateTimeField(auto_now_add = True)

class Meta:
    verbose_name_plural = "vendor"