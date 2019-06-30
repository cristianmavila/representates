from django.contrib import admin
from categories.models import Categories
from .models import Products, ProductsTypes

class ProductCategoryInline(admin.TabularInline):
  model = Categories

class ProductTypesInline(admin.TabularInline):
  model = ProductsTypes

class ProductAdmin(admin.ModelAdmin):
  inlines = [
    ProductTypesInline
  ]
  class Meta:
    model: Products

admin.site.register(Products, ProductAdmin)

