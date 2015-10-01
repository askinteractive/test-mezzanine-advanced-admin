# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_extra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('first_name', models.CharField(max_length=100, verbose_name=b'First name')),
                ('last_name', models.CharField(max_length=100, verbose_name=b'Last name')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
