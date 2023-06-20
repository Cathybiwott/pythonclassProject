from django.db import models

class User_Login(models.Model):
    name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 33)
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add = True)
    
