# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0006_auto_20150309_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-from_time']},
        ),
        migrations.AlterField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
