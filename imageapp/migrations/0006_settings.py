# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import imageapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0005_auto_20141110_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_pic', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/workspace/image_space/photos/profile_pics'), upload_to=imageapp.models.get_profile_pic_name)),
                ('user', models.ForeignKey(related_name='settings', to='imageapp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
