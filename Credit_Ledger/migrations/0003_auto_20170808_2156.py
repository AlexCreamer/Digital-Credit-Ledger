# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 00:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Credit_Ledger', '0002_auto_20170720_0051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
