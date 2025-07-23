from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()

    def __str__(self):
        return self.title
