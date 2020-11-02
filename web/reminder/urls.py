from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from reminder import views
from reminder.views import NotificationViewSet

notification_list = NotificationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
notification_detail = NotificationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path(r'notifications/', notification_list, name='notification-list'),
    path(r'notification/<int:pk>/', notification_detail, name='notification-detail'),
    path(r'api/users', views.UserCreate.as_view(), name='user-create'),
    path(r'api-token-auth/', obtain_auth_token, name='api_token_auth')
]
