# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='training_set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factor1', models.IntegerField()),
                ('factor2', models.IntegerField()),
                ('red', models.IntegerField()),
                ('green', models.IntegerField()),
                ('nir', models.IntegerField()),
                ('mir', models.IntegerField()),
                ('rs1', models.IntegerField()),
                ('rs2', models.IntegerField()),
                ('dem', models.IntegerField()),
                ('decision', models.CharField(max_length=255)),
            ],
        ),
    ]
