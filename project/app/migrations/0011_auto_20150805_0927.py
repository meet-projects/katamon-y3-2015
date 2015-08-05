# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150804_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default=b'', max_length=60),
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='account',
            name='isOrganization',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='name',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default=b'', max_length=15),
        ),
        migrations.AddField(
            model_name='account',
            name='website',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='isPalestinian',
            field=models.BooleanField(default=b''),
        ),
        migrations.AlterField(
            model_name='event',
            name='accounts',
            field=models.ManyToManyField(related_name='customer_events', to='app.Account'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(related_name='org_events', default=None, to='app.Account'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.CharField(max_length=100),
        ),
    ]
