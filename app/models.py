from django.db import models
from django.utils import timezone


class KeyValue(models.Model):
    # TODO: Add user attribute
    created_at = models.DateTimeField("Time when record inserted", default=timezone.now)
    key = models.SlugField(unique=True)
    # Not BinaryField, only texts are allowed!
    value = models.TextField()
