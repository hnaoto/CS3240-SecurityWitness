# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20150326_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('owner_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='folder_id',
            field=models.IntegerField(default=777),
        ),
        migrations.AlterField(
            model_name='report',
            name='long_text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='report',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
