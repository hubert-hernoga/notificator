# Generated by Django 3.1.2 on 2020-11-02 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificator', '0002_auto_20201102_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
