# Generated by Django 2.1.1 on 2018-10-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_donor_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='date_donated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='static/profiles/%Y/%m/%d'),
        ),
    ]
