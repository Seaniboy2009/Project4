# Generated by Django 3.2.16 on 2023-01-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_table_num_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='num_seats',
            field=models.CharField(choices=[(1, 'Table for 2'), (2, 'Table for 4'), (3, 'Table for 5'), (4, 'Table for 6')], default='Table for 2', max_length=10),
        ),
    ]
