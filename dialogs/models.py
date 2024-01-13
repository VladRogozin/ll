from django.db import models


class Dialog(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.JSONField()
    dialog = models.JSONField()

    def __str__(self):
        return self.title

