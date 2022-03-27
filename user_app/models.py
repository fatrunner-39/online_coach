from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, default='Russia')
    city = models.CharField(max_length=100, default='Kaliningrad')
    about_self = models.TextField(blank=True)
    is_coach = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
