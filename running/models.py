from django.contrib.auth.models import User
from django.db import models
from user_app.models import Profile

from datetime import datetime


class Workout(models.Model):

    ''' Создаем тренировку '''

    title = models.CharField(max_length=150, blank=True, default='Пробежка')
    runners = models.ManyToManyField(User, through='Report', related_name='run_student')
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='run_coach')
    run_distance = models.FloatField(null=True, blank=True)
    for_runners = models.ManyToManyField(User, related_name='workouts', blank=True)


class Exercise(models.Model):

    ''' Создаем упражнение '''

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercises')
    type = models.CharField(max_length=50)
    distance = models.IntegerField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.type


class Report(models.Model):

    ''' Создаем отчет о проделанной тренировке '''

    runner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='run_report')
    training = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='run_report')
    training_date = models.DateTimeField(default=datetime.now())
    text_report = models.TextField()
    feeling_scores = models.IntegerField()
