# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-10 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import osf.models.validators
import osf.utils.datetime_aware_jsonfield
import osf.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0032_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftregistration',
            name='datetime_updated',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='fileversion',
            name='location',
            field=osf.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(blank=True, default=None, null=True, validators=[osf.models.validators.validate_location]),
        ),
        migrations.AlterField(
            model_name='guid',
            name='created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='recentlyaddedcontributor',
            name='date_added',
            field=osf.utils.fields.NonNaiveDateTimeField(default=django.utils.timezone.now),
        ),
    ]
