from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

from reminder.models import Notification


class IsUserNotification(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if view.action == 'retrieve':
            try:
                notification_pk = request.resolver_match.kwargs.get('pk')
                Notification.objects.get(pk=notification_pk, owner=user)
                Notification.objects.filter(participants__id=user.id).first()
                return True
            except ObjectDoesNotExist:
                pass
