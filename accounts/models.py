from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    department = models.CharField(max_length=200, null=False, blank=False)
    is_active = models.BooleanField(null=False, blank=False)
    is_admin = models.BooleanField(null=True, blank=True)

