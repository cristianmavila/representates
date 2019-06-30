from django.contrib import admin
from django.urls import path, include
from products.models import ProductsViewSet, ProductsTypesViewSet
from brands.models import BrandsViewSet
from categories.models import CategoriesViewSet
from rest_framework import routers, viewsets

admin.site.site_header = 'Sistema de pedidos'

# Rest API
router = routers.DefaultRouter()
router.register(r'products', ProductsViewSet, basename='products')
router.register(r'products-types', ProductsTypesViewSet, basename='prodtypes')
router.register(r'brands', BrandsViewSet)
router.register(r'categories', CategoriesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include(router.urls)),
    #path('produtos/', include("products.urls", namespace="products")
]
