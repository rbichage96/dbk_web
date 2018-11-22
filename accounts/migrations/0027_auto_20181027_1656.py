# Generated by Django 2.1.2 on 2018-10-27 16:56

import accounts.models
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20181027_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.RemoveField(
            model_name='news',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=accounts.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='news',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='donor',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=accounts.models.upload_location),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(help_text='One hundred character!', max_length=100),
        ),
    ]