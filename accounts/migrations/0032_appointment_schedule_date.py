# Generated by Django 2.1.2 on 2018-10-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20181030_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='schedule_date',
            field=models.DateTimeField(null=True),
        ),
    ]