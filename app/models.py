from django.db import models
from django.util import timezone


class KeyValue(models.Model):
    # TODO: Add user attribute
    created_at = models.DateTimeField(
        "Time when record inserted", default=timezone.now()
    )
    key = models.CharField(max_length=64, unique=True)
    value = models.TextField()
