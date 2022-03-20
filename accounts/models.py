from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass
    # avatar = models.URLField()
    #
    # # pass
    # def save(self, *args, **kwargs):
    #     secial_account = self.socialaccount_set.get(provider='github')
    #     self.avatar = secial_account.extra_data['avatar_url']
    #     super(CustomUser, self).save(*args, **kwargs)
