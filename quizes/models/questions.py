from django.db import models


class Question(models.Model):
    order = models.IntegerField()
    question_text = models.TextField()
    multiple = models.BooleanField(default=None)
    picture = models.URLField()

    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)

