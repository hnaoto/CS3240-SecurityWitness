# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 25, 20, 19, 54, 41806, tzinfo=utc)),
        ),
    ]
