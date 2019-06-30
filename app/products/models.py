# -*- coding: utf-8 -*-
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from brands.models import Brands, BrandsSerializer
from categories.models import Categories, CategoriesSerializer
from rest_framework import serializers, viewsets
from rest_framework.response import Response

class Products(models.Model):

  packageTypes = (
    ('1', 'Unitário'),
    ('6', '6 peças'),
    ('12', '12 peças'),
    ('20', '20 peças')
  )

  prodBrand = models.ForeignKey(
    Brands,
    verbose_name = _('Marca'),
    null=True, blank=True,
    related_name='brandname',
    on_delete=models.CASCADE
  )

  prodCat = models.ManyToManyField(
    Categories,
    verbose_name = _('Categoria'),
    related_name='categoryname'
  )

  name = models.CharField(
    verbose_name = _('Nome'),
    max_length=50,
    blank=False
  )

  description = models.TextField(
    verbose_name = _('Descrição'),
    blank=True,
    default=''
  )

  package = models.CharField(
    verbose_name = ('Embalagem'),
    max_length=20,
    choices=packageTypes,
    blank=True,
    default='1'
  )

  submit_date = models.DateTimeField(
    verbose_name = _('Data'),
    auto_now=True
  )

  class Meta:
    verbose_name = _('Produto')
    verbose_name_plural = _('Produtos')

  def __str__(self):
    return self.name

class ProductsTypes(models.Model):

  prod = models.ForeignKey(
    Products,
    verbose_name = _('Variações'),
    related_name='types',
    on_delete=models.CASCADE
  )

  name = models.CharField(
    verbose_name = _('Nome'),
    max_length=50,
    blank=False
  )

  class Meta:
    verbose_name = _('Variação')
    verbose_name_plural = _('Variações')

  def __str__(self):
    return self.name

class ProductsSerializer(serializers.ModelSerializer):
    prodBrand = BrandsSerializer(many=False, read_only=True)
    prodCat = CategoriesSerializer(many=True, read_only=True)
    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'prodBrand', 'prodCat', 'package')

class ProductsTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsTypes
        fields = ('id', 'name', 'prod')

class ProductsTypesViewSet(viewsets.ViewSet):

  def list(self, request):
    queryset = ProductsTypes.objects.all()
    serializer = ProductsTypesSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, prod=None):
    #queryset = ProductsTypes.objects.all()
    prods = get_object_or_404(queryset, prod=prod)
    serializer = ProductsTypesSerializer(prods)
    return Response(serializer.data)

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer