# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_report_kw'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='file2',
            field=models.FileField(blank=True, upload_to='./upload/'),
        ),
    ]
