# Generated by Django 2.1.2 on 2019-04-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0064_auto_20190427_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='amount_donated',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='static/news'),
        ),
    ]