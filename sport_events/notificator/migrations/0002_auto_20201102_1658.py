# Generated by Django 3.1.2 on 2020-11-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='league_flag',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
