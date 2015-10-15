# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0003_remove_coupon_discount_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_from',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_till',
            field=models.DateField(),
        ),
    ]
