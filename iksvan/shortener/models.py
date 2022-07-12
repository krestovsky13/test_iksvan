import uuid
from django.contrib.auth.models import User
from django.db import models


class Urls(models.Model):
    full_url = models.URLField()
    short_url = models.CharField(unique=True, blank=True, max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.short_url = str(uuid.uuid4())[:6]
        return super().save(*args, **kwargs)
