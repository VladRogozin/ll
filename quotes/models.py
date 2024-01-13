from django.db import models


class Quote(models.Model):
    original = models.TextField()
    translation = models.TextField()
    author = models.CharField(max_length=255)

