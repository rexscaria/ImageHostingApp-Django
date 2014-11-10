# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/workspace/image_space/photos'), upload_to=b'')),
                ('user', models.ForeignKey(to='imageapp.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
