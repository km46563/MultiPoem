from django.conf import settings
from django.db import models


class UserReport(models.Model):
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    reported_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reports')
    resolver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='resolved_user_reports')
    
    class ReportStatus(models.TextChoices):
        PENDING = 'PENDING', 'Oczekujący'
        USER_SAFE = 'USER_SAFE', 'Użytkownik jest bezpieczny'
        USER_BLOCKED = 'USER_BLOCKED', 'Zablokowano użytkownika'

    status = models.CharField(
            max_length=14,
            choices=ReportStatus.choices,
            default=ReportStatus.PENDING
            )



class PostReport(models.Model):
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    reported_post = models.ForeignKey('content.Post', on_delete=models.SET_NULL, null=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_reports')
    resolver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='resolved_post_reports')
    
    class ReportStatus(models.TextChoices):
        PENDING = 'PENDING', 'Oczekujący'
        POST_SAFE = 'POST_SAFE', 'Post jest bezpieczny'
        POST_DELETION = 'POST_DELETION', 'Usunięto post'
        USER_BLOCKED = 'USER_BLOCKED', 'Zablokowano użytkownika'

    status = models.CharField(
            max_length=14,
            choices=ReportStatus.choices,
            default=ReportStatus.PENDING
        )
