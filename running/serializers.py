from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Sum, F
from user_app.models import Profile


from .models import Exercise, Workout, Report


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'type', 'distance', 'duration', 'quantity']


class WorkoutSerializer(serializers.ModelSerializer):

    ''' При созддании или обновлении трентировки получаем общую дистанцию тренировки, суммируя
    дистанции каждого упражнения. '''

    coach = UserSerializer(read_only=True)
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'title', 'coach', 'run_distance', 'exercises', 'for_runners']

    def create(self, validated_data):
        exercises = validated_data.pop('exercises')
        validated_data['coach'] = self.context['request'].user
        workout = super().create(validated_data)
        for exercise in exercises:
            Exercise.objects.create(workout=workout, **exercise)
        run = Exercise.objects.filter(workout=workout).aggregate(distance=Sum(F(
            'distance') * F('quantity')))
        workout.run_distance = run['distance'] / 1000
        workout.save()
        return workout

    def update(self, instance, validated_data):
        exercises_data = validated_data.pop('exercises')
        exercises = (instance.exercises).all()
        exercises = list(exercises)
        instance.title = validated_data.get('title', instance.title)
        instance.run_distance = validated_data.get('run_distance', instance.run_distance)
        instance.for_runners.set(validated_data['for_runners'])

        for exercise_data in exercises_data:
            try:
                exercise = exercises.pop(0)
                exercise.type = exercise_data.get('type', exercise.type)
                exercise.distance = exercise_data.get('distance', exercise.distance)
                exercise.duration = exercise_data.get('duration', exercise.duration)
                exercise.quantity = exercise_data.get('quantity', exercise.quantity)
                exercise.save()
            except IndexError:
                Exercise.objects.create(workout=instance, **exercise_data)

        run = Exercise.objects.filter(workout=instance).aggregate(distance=Sum(F(
            'distance') * F('quantity'))/1000)
        instance.run_distance = run['distance']
        instance.save()

        return instance


class ReportSerializer(serializers.ModelSerializer):
    runner = UserSerializer(read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'runner', 'training', 'training_date', 'text_report', 'feeling_scores']

    def create(self, validated_data):
        validated_data['runner'] = self.context['request'].user
        return super().create(validated_data)
