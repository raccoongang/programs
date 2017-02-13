# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0011_auto_20160510_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
