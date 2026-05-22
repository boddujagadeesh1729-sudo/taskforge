from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_task_notification_email(email, title):
    send_mail(
        subject='Task Reminder - TaskForge',
        message=f'Reminder: Your task "{title}" is pending.',
        from_email='taskforge@example.com',
        recipient_list=[email],
        fail_silently=False,
    )

    return f'Email sent to {email}'
