# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_test_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_set',
            name='decisiontree',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test_set',
            name='knndist',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test_set',
            name='knnuniform',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test_set',
            name='svm',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
