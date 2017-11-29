# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_models', '0002_cards_c_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
