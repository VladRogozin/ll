from django.db import models


class New(models.Model):
    title = models.CharField(max_length=255)
    english_news = models.TextField()
    ukrainian_news = models.TextField()
    keywords = models.JSONField()
    questions = models.JSONField()
