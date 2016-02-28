# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_report_file2'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='datetime',
            field=models.CharField(default='YYYY-MM-DD', max_length=200),
        ),
    ]
