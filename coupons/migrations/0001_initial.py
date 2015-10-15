# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=255, blank=True)),
                ('short_desc', models.TextField(default=None)),
                ('long_desc', models.TextField(default=None)),
                ('discount_type', models.IntegerField()),
                ('discount_value', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('valid_till', models.DateTimeField()),
            ],
        ),
    ]
