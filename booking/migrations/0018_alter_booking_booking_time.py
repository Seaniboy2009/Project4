# Generated by Django 3.2.16 on 2023-01-10 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_auto_20230107_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.TimeField(choices=[(datetime.time(10, 0), '10 AM'), (datetime.time(11, 0), '11 AM'), (datetime.time(12, 0), '12 AM'), (datetime.time(13, 0), '1 PM'), (datetime.time(14, 0), '2 PM'), (datetime.time(15, 0), '3 PM'), (datetime.time(16, 0), '4 PM')]),
        ),
    ]
