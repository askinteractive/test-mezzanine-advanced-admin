# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('title', models.CharField(default=b'', max_length=200, verbose_name=b'Titre')),
                ('image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name=b'Image', blank=True)),
                ('short_content', mezzanine.core.fields.RichTextField(verbose_name='Description courte', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=200, blank=True)),
                ('page', models.ForeignKey(related_name='blocks', verbose_name=b'Page', blank=True, to='pages.RichTextPage', null=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Bloc statique',
                'verbose_name_plural': 'Blocs statiques',
            },
        ),
        migrations.CreateModel(
            name='PageImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('file', mezzanine.core.fields.FileField(max_length=200, verbose_name=b'Fichier')),
                ('description', models.CharField(max_length=200, verbose_name=b'Description', blank=True)),
                ('page', models.ForeignKey(related_name='images', verbose_name=b'Page', blank=True, to='pages.RichTextPage', null=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Image',
            },
        ),
    ]
