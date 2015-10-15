# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
                ('referee', models.ForeignKey(related_name='referrer', to=settings.AUTH_USER_MODEL)),
                ('referrer', models.ForeignKey(related_name='referrer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
