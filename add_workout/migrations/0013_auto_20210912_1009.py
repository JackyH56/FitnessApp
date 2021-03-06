# Generated by Django 3.2.7 on 2021-09-12 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_workout', '0012_alter_exerciseset_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseset',
            name='exercise',
            field=models.CharField(choices=[('bench', 'bench'), ('squat', 'squat'), ('deadlift', 'deadlift')], max_length=50),
        ),
        migrations.AlterField(
            model_name='exerciseset',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 12, 10, 9, 21, 883137)),
        ),
    ]
