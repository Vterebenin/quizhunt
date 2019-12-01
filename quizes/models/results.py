from django.db import models


class Result(models.Model):
    result_title = models.CharField(max_length=50)
    result_text = models.TextField()
    picture = models.URLField()
    points_to_earn = models.IntegerField(default=None)

    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)

