# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_event_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventCatergory',
            new_name='EventCategory',
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default=-1, to='app.EventCatergory'),
        ),
    ]
