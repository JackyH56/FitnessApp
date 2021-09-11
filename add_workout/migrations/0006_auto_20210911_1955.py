# Generated by Django 3.2.7 on 2021-09-11 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_workout', '0005_exerciseset_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseset',
            name='exercise',
            field=models.CharField(choices=[('bench', 'BENCH'), ('squat', 'SQUAT'), ('deadlift', 'DEADLIFT')], max_length=50),
        ),
        migrations.AlterField(
            model_name='exerciseset',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 11, 19, 55, 53, 139184)),
        ),
    ]