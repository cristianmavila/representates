# Generated by Django 2.2.2 on 2019-06-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='products',
            name='package',
            field=models.CharField(blank=True, choices=[('1', 'Unitário'), ('6', '6 peças'), ('12', '12 peças'), ('20', '20 peças')], default='1', max_length=20, verbose_name='Embalagem'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
