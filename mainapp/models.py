from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField
from django.db.models.functions import Now

class User(AbstractUser):
    class UserStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Aktywny'
        BLOCKED = 'BLOCKED', 'Zablokowany'

    status = models.CharField(
            max_length=10,
            choices=UserStatus.choices,
            default=UserStatus.ACTIVE
            )


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField()
    createdAt = models.DateTimeField(db_default=Now())
    mood = CharField = models.CharField(max_length=50)

    class PostType(models.TextChoices):
        STANDARD = 'STANDARD', 'Standardowy'
        LIMITED_COLLAB = 'LIMITED_COLLAB', 'Limitowana kolaboracja'
        UNLIMITED_COLLAB = 'UNLIMITED_COLLAB', 'Nielimitowana kolaboracja'

    status = models.CharField(
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
    createdAt = models.DateTimeField(db_default=Now())
    resolvedAt = models.DateTimeField()
    note = CharField()

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
    note = models.CharField()
    createdAt = models.DateTimeField(db_default=Now())
    
    class ReportStatus(models.TextChoices):
        PENDING = 'PENDING', 'Oczekujący'
        POST_SAVE = 'POST_SAVE', 'Post jest bezpieczny'
        POST_DELETION = 'POST_DELETION', 'Usunięto post'
        USER_BLOCKED = 'USER_BLOCKED', 'Zablokowano użytkownika'

    status = models.CharField(
            max_length=14,
            choices=ReportStatus.choices,
            default=ReportStatus.PENDING
            )

class UserReport(models.Model):
    note = models.CharField()
    createdAt = models.DateTimeField(db_default=Now())
    
    class ReportStatus(models.TextChoices):
        PENDING = 'PENDING', 'Oczekujący'
        USER_SAVE = 'USER_SAVE', 'Użytkownik jest bezpieczny'
        USER_BLOCKED = 'USER_BLOCKED', 'Zablokowano użytkownika'

    status = models.CharField(
            max_length=14,
            choices=ReportStatus.choices,
            default=ReportStatus.PENDING
            )


