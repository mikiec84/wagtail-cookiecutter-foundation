# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-30 15:39
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogindexpage_feed_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock()), ('markdown', wagtailmarkdown.fields.MarkdownBlock(icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.core.blocks.RawHTMLBlock()))),
        ),
    ]
