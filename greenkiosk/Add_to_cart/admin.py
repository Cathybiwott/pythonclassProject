from django.contrib import admin
from .models import Add_to_cart

class Add_to_cartAdmin(admin.ModelAdmin):
    list_display = ("name","price","image","description")

admin.site.register(Add_to_cart,Add_to_cartAdmin)


