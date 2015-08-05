# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_auto_20150805_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isPalestinian', models.BooleanField(default=b'')),
                ('name', models.CharField(default=b'', max_length=30)),
                ('phone_number', models.CharField(default=b'', max_length=15)),
                ('address', models.CharField(default=b'', max_length=60)),
                ('description', models.CharField(default=b'', max_length=300)),
                ('website', models.CharField(default=b'', max_length=100)),
                ('isOrganization', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('address', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=300)),
                ('group_size', models.IntegerField()),
                ('accounts', models.ManyToManyField(related_name='customer_events', to='app.Account')),
                ('organization', models.ForeignKey(related_name='org_events', default=None, to='app.Account')),
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
        migrations.AddField(
            model_name='chat',
            name='event',
            field=models.OneToOneField(to='app.Event'),
        ),
    ]
