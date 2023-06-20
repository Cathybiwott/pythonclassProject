from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ("name","price","total","image","description")

admin.site.register(Order,OrderAdmin)


