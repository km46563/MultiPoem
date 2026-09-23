from django.db import models
from django.conf import settings


class Follow(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["follower", "followed"], name="unique_follow"),
            models.CheckConstraint(condition=~models.Q(follower=models.F("followed")), name="prevent_self_follow")
]
