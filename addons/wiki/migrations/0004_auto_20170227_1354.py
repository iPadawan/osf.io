# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-27 19:54
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import osf.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('addons_wiki', '0003_auto_20170119_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodewikipage',
            name='date',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
    ]
