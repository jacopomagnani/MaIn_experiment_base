# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-25 06:10
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20180912_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='major',
            field=otree.db.models.StringField(blank=True, choices=[('Science, technology, engineering and mathematics', 'Science, technology, engineering and mathematics'), ('Social sciences', 'Social sciences'), ('Art and humanities', 'Art and humanities')], max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='sex',
            field=otree.db.models.StringField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10000, null=True),
        ),
    ]