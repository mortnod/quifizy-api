# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_auto_20160417_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='songs',
            field=models.ManyToManyField(related_name='category', to='songs.Song'),
        ),
    ]