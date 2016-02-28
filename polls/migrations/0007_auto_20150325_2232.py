# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150325_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 22, 32, 37, 554067, tzinfo=utc)),
        ),
    ]
