from django.contrib import admin
from .models import Brands

class BrandAdmin(admin.ModelAdmin):
  pass

admin.site.register(Brands, BrandAdmin)

