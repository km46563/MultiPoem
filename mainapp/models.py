from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    mood = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
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


class PostReport(models.Model):
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    reported_post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_reports')
    resolver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='resolved_post_reports')
    
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


class UserReport(models.Model):
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    reported_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reports')
    resolver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='resolved_user_reports')
    
    class ReportStatus(models.TextChoices):
        PENDING = 'PENDING', 'Oczekujący'
        USER_SAFE = 'USER_SAFE', 'Użytkownik jest bezpieczny'
        USER_BLOCKED = 'USER_BLOCKED', 'Zablokowano użytkownika'

    status = models.CharField(
            max_length=14,
            choices=ReportStatus.choices,
            default=ReportStatus.PENDING
            )


class Profile(models.Model):
    description = models.TextField(blank=True)
    # TODO: Here will be some kind of background; gradient or png/jpg, I don't know yet
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Follow(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["follower", "followed"], name="unique_follow"),
            models.CheckConstraint(condition=~models.Q(follower=models.F("followed")), name="prevent_self_follow")
        ]
   

class SavedPost(models.Model):
    saved_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_save")
        ]



class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "post"], name="unique_like")
        ]


class Comment(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')


class FeedSession(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class PostView(models.Model):
    position = models.PositiveIntegerField()
    viewed_at = models.DateTimeField(auto_now_add=True)
    feed_session = models.ForeignKey(FeedSession, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['position', 'feed_session'], name='unique_position_in_feed_session')
        ]
