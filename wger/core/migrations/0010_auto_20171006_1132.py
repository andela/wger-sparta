# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-06 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0001_initial'),
        ('core', '0009_auto_20160303_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='added_by',
            field=models.ForeignKey(blank=True, help_text='These are the users that have been added viathe rest api', null=True, on_delete=django.db.models.deletion.CASCADE, to='authtoken.Token', verbose_name='Added by external via rest api'),
        ),
        migrations.AlterField(
            model_name='license',
            name='full_name',
            field=models.CharField(help_text='If a license has been localized, e.g. the Creative Commons licenses for the different countries, add them as separate entries here.', max_length=60, verbose_name='Full name'),
        ),
    ]
