from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from reminder import views

urlpatterns = [
    path(r'api/users', views.UserCreate.as_view(), name='user-create'),
    path(r'api-token-auth/', obtain_auth_token, name='api_token_auth')
]
