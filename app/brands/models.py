# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, viewsets

class Brands(models.Model):

  name = models.CharField(
    verbose_name=_('Nome'),
    max_length=50,
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
    verbose_name = _("Marca")
    verbose_name_plural = _("Marcas")

  def __str__(self):
    return self.name


class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ('id', 'name')

class BrandsViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
