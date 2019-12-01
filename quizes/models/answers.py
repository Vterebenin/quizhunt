from django.db import models


class Answer(models.Model):
    answer_text = models.TextField()
    order = models.IntegerField()
    correct = models.BooleanField()
    cost = models.IntegerField(default=None)

    question = models.ForeignKey('Question', on_delete=models.CASCADE)

