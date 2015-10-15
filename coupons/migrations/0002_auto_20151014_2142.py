# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='long_desc',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='coupon',
            name='short_desc',
        ),
        migrations.AddField(
            model_name='coupon',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 21, 42, 43, 656593, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 21, 42, 47, 421055, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 21, 42, 49, 824440, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
