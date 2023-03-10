# Generated by Django 3.2.16 on 2023-01-02 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0005_auto_20230102_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='table',
            name='time',
            field=models.CharField(choices=[('8:00', '8:00'), ('9:00', '9:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00')], default='8:00', max_length=10),
        ),
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Awaiting'), (1, 'Approved')], default=0),
        ),
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
