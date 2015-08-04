# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_event_group_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
