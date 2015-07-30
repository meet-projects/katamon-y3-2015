# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150730_1221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account',
            new_name='user',
        ),
    ]
