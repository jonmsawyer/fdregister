# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0003_auto_20150309_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='confirmation_code',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
    ]
