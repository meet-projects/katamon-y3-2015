# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150803_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group_size',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
    ]
