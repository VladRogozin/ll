from django.db import models


class Fact(models.Model):
    fact_english = models.CharField(max_length=400, default='none')
    fact_ukrainian = models.CharField(max_length=400, default='none')
    words = models.JSONField(default=dict)
    word_level = models.CharField(max_length=2, default='none')

