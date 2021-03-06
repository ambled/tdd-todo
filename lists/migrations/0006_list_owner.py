# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-15 04:50
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0005_list_item_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(to_field='email', blank=True, null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
