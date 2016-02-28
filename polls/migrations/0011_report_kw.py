# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_report_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='kw',
            field=models.CharField(default='', max_length=200),
        ),
    ]
