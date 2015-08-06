# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_eventcatergory'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcatergory',
            name='name2',
            field=models.CharField(default='Afafaf', max_length=30),
            preserve_default=False,
        ),
    ]
