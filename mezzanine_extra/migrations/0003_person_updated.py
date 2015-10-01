# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_extra', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 1, 21, 16, 19, 638507), verbose_name=b'Updated at', auto_now=True),
            preserve_default=False,
        ),
    ]
