from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Report, Workout
from .serializers import ReportSerializer, WorkoutSerializer
from .permissions import IsOnlyCoach, IsOwnerOrReadOnly


class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    # permission_classes = [IsOnlyCoach]

    def get_queryset(self):

        '''Если пользователь является тренером, в queryset возвращаем все тренировки этого
        тренера.
        Если пользователь является бегуном, то возвращаем только те тренировки, для кого они
        написаны'''

        user = self.request.user

        if user.profile.is_coach == True:
            return Workout.objects.filter(coach=user)
        else:
            return user.workouts.all().order_by('id')

    def get_permissions(self):

        '''Создавать и обновлять тренировку может только тренер'''

        if self.action in ['create', 'update', 'partial_update', 'delete']:
            return [IsOnlyCoach()]
        return []


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all().order_by('id')
    serializer_class = ReportSerializer
    '''Просматривать отчеты могут только авторизованные пользователи. 
    Изменять и удалять отчеты могут только авторы отчетов'''
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
