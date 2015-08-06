# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_eventcatergory_name2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='eventCatergory',
        ),
    ]
