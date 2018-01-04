# Generated by Django 2.0 on 2018-01-04 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180104_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='age',
            field=models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(55)]),
        ),
    ]
