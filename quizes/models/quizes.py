from django.db import models


class Quiz(models.Model):  # модель одного теста
    title = models.CharField(max_length=50)
    desc = models.TextField()
    visited = models.BooleanField(default=False)
    solved = models.BooleanField(default=False)
    bank = models.IntegerField(default=0)

    # user_id = models.ForeignKey(on_delete=models.CASCADE)
