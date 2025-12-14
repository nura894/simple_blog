from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Course

@receiver(post_save, sender=Course)
def send_email_when_course_created(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Course Created",
            message=f"New course: {instance.title}",
            from_email="admin@example.com",
            recipient_list=[instance.created_by.email],
        )
