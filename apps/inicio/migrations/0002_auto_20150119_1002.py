# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfiles',
            old_name='usuerio',
            new_name='usuario',
        ),
    ]
