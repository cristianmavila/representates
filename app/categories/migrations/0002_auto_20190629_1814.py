# Generated by Django 2.2.2 on 2019-06-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
    ]
