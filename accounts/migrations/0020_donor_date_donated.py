# Generated by Django 2.1.1 on 2018-10-10 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='date_donated',
            field=models.DateField(null=True),
        ),
    ]