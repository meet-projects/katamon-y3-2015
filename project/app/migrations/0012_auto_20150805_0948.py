# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150805_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppAccount',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('emailaddress', models.CharField(unique=True, max_length=75, db_column='emailAddress')),
                ('password', models.CharField(max_length=30)),
                ('ispalestinian', models.BooleanField(db_column='isPalestinian')),
                ('birthday', models.DateTimeField()),
            ],
            options={
                'db_table': 'app_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('user_id', models.IntegerField()),
                ('content_type_id', models.IntegerField(null=True, blank=True)),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_key', models.CharField(unique=True, max_length=40)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='accounts',
        ),
        migrations.RemoveField(
            model_name='event',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='message',
            name='account',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.RemoveField(
            model_name='volunteerhoursbadge',
            name='account',
        ),
        migrations.RemoveField(
            model_name='volunteertimesbadge',
            name='account',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='VolunteerHoursBadge',
        ),
        migrations.DeleteModel(
            name='VolunteerTimesBadge',
        ),
    ]
