# Generated by Django 2.1.2 on 2019-04-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0060_auto_20190425_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
