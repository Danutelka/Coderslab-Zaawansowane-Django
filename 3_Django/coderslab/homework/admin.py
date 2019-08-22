from django.contrib import admin
from django.contrib.admin import ModelAdmin
from homework.models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]