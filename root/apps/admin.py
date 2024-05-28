

from django.contrib import admin
from .models import Products,Users


@admin.register(Products)
class TaskAdmin(admin.ModelAdmin):
    fields = ['name', 'description','price','image']


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    fields = ['username','email','password']
