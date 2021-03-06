# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-09 20:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0041_auto_20170308_1932'),
    ]

    operations = [
        migrations.RunSQL(
            [
                'CREATE INDEX osf_abstractnode_registered_date_index ON public.osf_abstractnode (registered_date DESC);',
                "CREATE INDEX osf_abstractnode_registration_pub_del_type_index ON public.osf_abstractnode (is_public, is_deleted, type) WHERE is_public=TRUE and is_deleted=FALSE and type = 'osf.registration';"
                "CREATE INDEX osf_abstractnode_node_pub_del_type_index ON public.osf_abstractnode (is_public, is_deleted, type) WHERE is_public=TRUE and is_deleted=FALSE and type = 'osf.node';"
                "CREATE INDEX osf_abstractnode_collection_pub_del_type_index ON public.osf_abstractnode (is_public, is_deleted, type) WHERE is_public=TRUE and is_deleted=FALSE and type = 'osf.collection';"
            ],
            [
                'DROP INDEX public.osf_abstractnode_registered_date_index RESTRICT;'
                'DROP INDEX public.osf_abstractnode_registration_pub_del_type_index RESTRICT;'
                'DROP INDEX public.osf_abstractnode_node_pub_del_type_index RESTRICT;'
                'DROP INDEX public.osf_abstractnode_collection_pub_del_type_index RESTRICT;'
             ]
        )
    ]
