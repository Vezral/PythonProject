# Generated by Django 2.0.5 on 2018-05-15 11:20

import captive_portal.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllocatedBandwidth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_speed_in_Kbps', models.FloatField(default=0)),
                ('upload_speed_in_Kbps', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RemoveWiFiTokenScheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='WiFiToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True)),
                ('expiration_time', models.DateTimeField()),
                ('qr_code', models.FileField(upload_to=captive_portal.models.upload_directory)),
                ('current_connected', models.IntegerField(default=0)),
                ('max_connected', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WifiTokenAssociatedIPAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100, unique=True)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='captive_portal.WiFiToken')),
            ],
        ),
    ]
