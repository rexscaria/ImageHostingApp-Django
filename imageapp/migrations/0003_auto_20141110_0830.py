# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='_password',
            new_name='password',
        ),
    ]
