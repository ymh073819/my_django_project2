# Generated by Django 2.0 on 2018-09-05 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('START_TIME', models.DateTimeField()),
                ('T', models.IntegerField()),
                ('NET_ELE', models.CharField(max_length=50)),
                ('SECTOR_NAME', models.IntegerField()),
                ('RRC_BUILD', models.IntegerField()),
                ('RRC_REQUEST', models.IntegerField()),
                ('RRC_RATE', models.FloatField()),
                ('RAB_SUCCESS', models.IntegerField()),
                ('RAB_TRY', models.IntegerField()),
                ('RAB_RATE', models.FloatField()),
                ('eNodeB_TIME', models.IntegerField()),
                ('SECTOR_TIME', models.IntegerField()),
                ('RAB_DROP_RATE', models.FloatField()),
                ('CONN_RATE', models.FloatField()),
                ('RESET_TIME', models.IntegerField()),
                ('ABNORMAL_TIME', models.IntegerField()),
                ('SUCCESS_TIME', models.IntegerField()),
                ('WIRELESS_DROP_RATE', models.FloatField()),
                ('eNodeB_IN_DIF_SUCCESS', models.IntegerField()),
                ('eNodeB_IN_DIF_TRY', models.IntegerField()),
                ('eNodeB_IN_SIM_SUCCESS', models.IntegerField()),
                ('eNodeB_IN_SIM_TRY', models.IntegerField()),
                ('eNodeB_OUT_DIF_SUCCESS', models.IntegerField()),
                ('eNodeB_OUT_DIF_TRY', models.IntegerField()),
                ('eNodeB_OUT_SIM_SUCCESS', models.IntegerField()),
                ('eNodeB_OUT_SIM_TRY', models.IntegerField()),
                ('eNodeB_IN_RATE', models.FloatField()),
                ('eNodeB_OUT_RATE', models.FloatField()),
                ('SIM_RATE', models.FloatField()),
                ('DIF_RATE', models.FloatField()),
                ('TOTAL_SUCCESS_RATE', models.FloatField()),
                ('UP_BIT', models.IntegerField()),
                ('DOWN_BIT', models.IntegerField()),
                ('RRC_REBUILD_REQUEST', models.IntegerField()),
                ('RRC_REBUILD_RATE', models.FloatField()),
                ('REBUILD_SIM_IN_TIME', models.IntegerField()),
                ('REBUILD_DIF_IN_TIME', models.IntegerField()),
                ('REBUILD_SIM_OUT_TIME', models.IntegerField()),
                ('REBUILD_DIF_OUT_TIME', models.IntegerField()),
                ('eNB_REQUEST_TIME', models.IntegerField()),
                ('eNB_TRY_TIME', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tbCell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CITY', models.CharField(max_length=50)),
                ('SECTOR_ID', models.CharField(max_length=50)),
                ('SECTOR_NAME', models.CharField(max_length=50)),
                ('ENODEBID', models.CharField(max_length=50)),
                ('ENODEB_NAME', models.CharField(max_length=50)),
                ('EARFCN', models.IntegerField()),
                ('PCI', models.IntegerField()),
                ('PSS', models.IntegerField()),
                ('SSS', models.IntegerField()),
                ('TAC', models.IntegerField()),
                ('VENDOR', models.CharField(max_length=50)),
                ('LONGITUDE', models.FloatField()),
                ('LATITUDE', models.FloatField()),
                ('STYLE', models.CharField(max_length=50)),
                ('AZIMUTH', models.IntegerField()),
                ('HEIGHT', models.IntegerField()),
                ('ELECTTILT', models.IntegerField()),
                ('MECHTILT', models.IntegerField()),
                ('TOTLETILT', models.IntegerField()),
            ],
        ),
    ]
