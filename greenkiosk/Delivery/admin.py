from django.contrib import admin

from .models import Delivery

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("name","price","image","description","address")

admin.site.register(Delivery,DeliveryAdmin)
