# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20150401_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='location',
            field=models.CharField(default='NA', max_length=200),
        ),
    ]
