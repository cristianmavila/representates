# Generated by Django 2.2.2 on 2019-06-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190628_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prodBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete='Marca', related_name='brandname', to='brands.Brands'),
        ),
        migrations.AlterField(
            model_name='products',
            name='prodCat',
            field=models.ForeignKey(blank=True, null=True, on_delete='Categoria', related_name='categoryname', to='categories.Categories'),
        ),
    ]
