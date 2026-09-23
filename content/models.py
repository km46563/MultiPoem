from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    mood = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="continuations")

    class PostType(models.TextChoices):
        STANDARD = 'STANDARD', 'Standardowy'
        LIMITED_COLLAB = 'LIMITED_COLLAB', 'Limitowana kolaboracja'
        UNLIMITED_COLLAB = 'UNLIMITED_COLLAB', 'Nielimitowana kolaboracja'

    post_type = models.CharField(
            max_length=20,
            choices=PostType.choices,
            default=PostType.STANDARD
            )

    class PostGenre(models.TextChoices):
        POEM = 'POEM', 'Wiersz'
        STORY = 'STORY', 'Opowiadanie'
        JOKE = 'JOKE', 'Żart'
        EPIGRAM = 'EPIGRAM', 'Fraszka'
        APHORISM = 'APHORISM', 'Aforyzm'
        FAIRYTALE = 'FAIRYTALE', 'Bajka'
        OTHER = 'OTHER', 'Inne'

    genre = models.CharField(
            max_length=20,
            choices=PostGenre.choices,
            default=PostGenre.OTHER
            )

    def __str__(self):
        return f'{self.title}'


class CollabRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    note = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class RequestStatus(models.TextChoices):
        PENDING = 'PENDING', 'Oczekujący',
        ACCEPTED = 'ACCEPTED', 'Zaakceptowany'
        REJECTED = 'REJECTED', 'Odrzucony'

    status = models.CharField(
            max_length=10,
            choices=RequestStatus.choices,
            default=RequestStatus.PENDING
            )



class SavedPost(models.Model):
    saved_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_save")
        ]



class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_like")
        ]

       

class Comment(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
