# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150325_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 3, 26, 3, 54, 26, 587964, tzinfo=utc))),
                ('long_text', models.CharField(max_length=1000)),
                ('short_text', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(default=0)),
                ('private', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='./upload/')),
            ],
        ),
        migrations.DeleteModel(
            name='Reports',
        ),
    ]
