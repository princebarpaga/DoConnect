# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-18 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doconnect_website', '0003_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('userquestion', models.CharField(max_length=200)),
                ('priorityid', models.IntegerField()),
            ],
        ),
    ]