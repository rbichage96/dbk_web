# Generated by Django 2.1.2 on 2018-11-26 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20181124_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='county',
            name='code',
        ),
    ]
