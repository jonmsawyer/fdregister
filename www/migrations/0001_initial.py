# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('short_title', models.CharField(max_length=20)),
                ('thumbnail', models.FileField(null=True, upload_to=b'', blank=True)),
                ('full_pic', models.FileField(null=True, upload_to=b'', blank=True)),
                ('from_time', models.DateTimeField()),
                ('to_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('is_closed', models.BooleanField()),
                ('is_published', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmation_code', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('age_range', models.CharField(default=b'under13', max_length=7, choices=[(b'under13', b'Under 13'), (b'13to20', b'13 through 20'), (b'over21', b'21 and over')])),
                ('notify_future', models.BooleanField()),
                ('comments', models.TextField(null=True, blank=True)),
                ('referral', models.CharField(max_length=256)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(to='www.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
