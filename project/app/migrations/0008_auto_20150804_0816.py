# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150803_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('account', models.ForeignKey(to='app.Account')),
                ('chat', models.ForeignKey(to='app.Chat')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerHoursBadge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('hours_requirement', models.IntegerField()),
                ('account', models.ManyToManyField(to='app.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VolunteerTimesBadge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('times_requirement', models.IntegerField()),
                ('account', models.ManyToManyField(to='app.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='AddEvent',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='number',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(default=None, to='app.Organization'),
        ),
        migrations.AddField(
            model_name='chat',
            name='event',
            field=models.OneToOneField(to='app.Event'),
        ),
    ]
