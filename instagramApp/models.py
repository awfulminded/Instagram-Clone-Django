from django.db import models
from django.contrib.auth.models import User

class ProfileOwner(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True

class Profile(ProfileOwner):
    username = models.CharField(max_length=255, null=True)
    avatar = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.username
