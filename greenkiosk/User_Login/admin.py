from django.contrib import admin
from .models import User_Login

class User_LoginAdmin(admin.ModelAdmin):
    list_display = ("name","email","image","date_created")

admin.site.register(User_Login,User_LoginAdmin)


