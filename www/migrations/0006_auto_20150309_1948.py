# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0005_auto_20150309_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='referral',
            field=models.CharField(max_length=256, null=True, blank=True),
            preserve_default=True,
        ),
    ]
