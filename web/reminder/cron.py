from datetime import datetime

from django.core.mail import send_mail

from reminder.models import Notification
from reminder_service import settings


def send_email_notification():
    current_date = datetime.now()
    notifications = Notification.objects.filter(event_date__lte=current_date, is_event_data_send=False)
    for notification in notifications:
        subject = 'Notification reminder'
        message = f'Task notification called {notification.title}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [participant.email for participant in notification.participants]
        notification.is_event_data_send = True
        notification.save()
        send_mail(subject, message, email_from, recipient_list)
