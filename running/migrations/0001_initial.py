# Generated by Django 4.0.1 on 2022-03-22 10:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_report', models.TextField()),
                ('feeling_scores', models.IntegerField()),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_report', to='user_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Пробежка', max_length=150)),
                ('training_date', models.DateTimeField(default=datetime.datetime(2022, 3, 22, 12, 48, 38, 717777))),
                ('run_distance', models.FloatField(blank=True, null=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_coach', to='user_app.profile')),
                ('runner', models.ManyToManyField(related_name='run_student', through='running.Report', to='user_app.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='run_report', to='running.workout'),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('distance', models.IntegerField(blank=True, null=True)),
                ('duration', models.DurationField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='running.workout')),
            ],
        ),
    ]