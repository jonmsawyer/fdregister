# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0002_auto_20150309_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_title',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
