# Generated by Django 2.1.2 on 2019-04-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20190427_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
