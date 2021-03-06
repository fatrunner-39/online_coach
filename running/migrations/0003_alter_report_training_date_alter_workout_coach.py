# Generated by Django 4.0.1 on 2022-03-22 15:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('running', '0002_rename_from_user_report_runner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='training_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 22, 17, 46, 37, 847872)),
        ),
        migrations.AlterField(
            model_name='workout',
            name='coach',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_coach', to=settings.AUTH_USER_MODEL),
        ),
    ]
