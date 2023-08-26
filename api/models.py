from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    answer = models.IntegerField()

    def __str__(self):
        return self.title
