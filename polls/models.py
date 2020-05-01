import datetime

from django.db import models
from django.utils import timezone


# В нашем приложении для опросов создадим две модели: Вопрос и
# Выбор. Вопрос имеет вопрос и дату публикации. Выбор имеет
# два поля: текст выбора и подсчет голосов. Каждый выбор связан
# с вопросом.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # если дата публик больше, равна сегодняшней дате минус один день
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
