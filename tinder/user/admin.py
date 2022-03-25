from django.contrib import admin
from .models import Client
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model=Client
    list_display = ('email', 'name', 'surname', 'is_staff')

admin.site.register(Client, CustomUserAdmin)

# Register your models here.
