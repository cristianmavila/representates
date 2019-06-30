# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, viewsets

class Categories(models.Model):

  name = models.CharField(
    verbose_name=_('Nome'),
    max_length=50,
    unique=True,
    blank=False
  )

  description = models.TextField(
    verbose_name=_('Descrição'),
    blank=True,
    default=''
  )

  submit_date = models.DateTimeField(
    _('Data'),
    auto_now=True
  )

  class Meta:
    verbose_name = _("Categoria")
    verbose_name_plural = _("Categorias")

  def __str__(self):
    return self.name

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name')

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer