from rest_framework import permissions


class IsOnlyCoach(permissions.BasePermission):
    message = 'You must be a coach'

    def has_permission(self, request, view):
        return request.user.profile.is_coach


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.runner == request.user
