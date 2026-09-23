from django.conf import settings
from django.db import models





class FeedSession(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class PostView(models.Model):
    position = models.PositiveIntegerField()
    viewed_at = models.DateTimeField(auto_now_add=True)
    feed_session = models.ForeignKey(FeedSession, on_delete=models.CASCADE)
    post = models.ForeignKey('content.Post', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['position', 'feed_session'], name='unique_position_in_feed_session')
        ]
