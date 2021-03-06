from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets

from reminder.models import Notification
from reminder.permissions import IsUserNotification
from reminder.serializers import UserSerializer, NotificationSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated & IsUserNotification,)

