from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","stock","price","description")

admin.site.register(Product,ProductAdmin)
