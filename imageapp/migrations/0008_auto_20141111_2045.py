# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import imageapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0007_auto_20141111_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='profile_pic',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/workspace/image_space/photos/profile_pics'), upload_to=imageapp.models.get_profile_pic_name),
            preserve_default=True,
        ),
    ]
