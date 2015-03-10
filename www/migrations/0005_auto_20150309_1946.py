# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0004_auto_20150309_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='confirmation_code',
            field=models.CharField(default=1, max_length=40, blank=True),
            preserve_default=False,
        ),
    ]
