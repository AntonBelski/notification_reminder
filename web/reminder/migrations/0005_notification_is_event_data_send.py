# Generated by Django 3.1.2 on 2020-11-04 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0004_auto_20201102_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_event_data_send',
            field=models.BooleanField(default=False),
        ),
    ]
