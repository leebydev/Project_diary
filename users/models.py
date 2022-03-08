from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Member(AbstractUser):
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT,
                              blank=True,
                              null=True)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname

