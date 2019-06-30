from django.contrib import admin
from .models import Categories

class CategoryAdmin(admin.ModelAdmin):
  pass

admin.site.register(Categories, CategoryAdmin)

