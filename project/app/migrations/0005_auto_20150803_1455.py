# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150803_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='time',
            new_name='duration',
        ),
    ]
