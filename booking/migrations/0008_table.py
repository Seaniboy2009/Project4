# Generated by Django 3.2.16 on 2023-01-02 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0007_delete_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(unique=True)),
                ('num_seats', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('booked', models.BooleanField(default=False)),
                ('time', models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00')], default='8:00', max_length=10)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
