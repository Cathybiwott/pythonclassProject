from django.contrib import admin

# Register your models here.
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone","password")

admin.site.register(Customer,CustomerAdmin)
