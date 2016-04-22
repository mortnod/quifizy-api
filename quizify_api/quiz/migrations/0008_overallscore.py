# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 10:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20160421_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='OverallScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overall_score', to='quiz.Game')),
            ],
        ),
    ]
