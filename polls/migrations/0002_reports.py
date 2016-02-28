# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 3, 25, 20, 18, 32, 120713))),
                ('long_text', models.CharField(max_length=1000)),
                ('short_text', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(default=0)),
                ('private', models.BooleanField(default=True)),
                ('file', models.FileField(upload_to='./upload/')),
            ],
        ),
    ]
