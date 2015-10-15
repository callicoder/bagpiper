# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20151014_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='discount_type',
        ),
    ]
