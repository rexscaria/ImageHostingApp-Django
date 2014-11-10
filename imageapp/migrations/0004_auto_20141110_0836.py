# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0003_auto_20141110_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='user',
            field=models.ForeignKey(related_name='pictures', to='imageapp.User'),
            preserve_default=True,
        ),
    ]
