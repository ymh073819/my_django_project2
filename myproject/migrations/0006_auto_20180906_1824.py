# Generated by Django 2.0 on 2018-09-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_auto_20180906_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='SECTOR_DETAIL',
            field=models.CharField(max_length=100),
        ),
    ]
