# Generated by Django 3.2.16 on 2023-01-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_auto_20230113_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.CharField(default='menu item', max_length=100),
        ),
    ]
