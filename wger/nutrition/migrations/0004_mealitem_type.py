# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-23 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0003_auto_20171019_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealitem',
            name='type',
            field=models.CharField(choices=[('PLANNED', 'Planned'), ('EATEN', 'Eaten')], default='PLANNED', max_length=20),
        ),
    ]
