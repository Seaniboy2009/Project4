# Generated by Django 3.2.16 on 2022-12-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20221226_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
