# Generated by Django 2.0 on 2018-09-06 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0008_auto_20180906_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi',
            name='SIM_RATE',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
