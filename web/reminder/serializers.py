from rest_framework import serializers

from .models import User, Notification


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'notifications', 'owned_notifications')


class NotificationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = ('title', 'description', 'location', 'creation_date', 'event_date', 'is_finished')
