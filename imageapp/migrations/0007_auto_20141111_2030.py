# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0006_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='profile_pic',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/workspace/image_space/photos/profile_pics'), upload_to=b''),
            preserve_default=True,
        ),
    ]
