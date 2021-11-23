from django.db import models
from question.constants import QUESTION_TYPES


class Survey(models.Model):
    name = models.TextField(max_length=50, verbose_name='Наименование опроса')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата начала опроса')
    end_date = models.DateField(verbose_name='Дата окончания опроса')
    description = models.TextField(max_length=255, verbose_name='Описание опроса')

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name='Опрос к которому относится вопрос')
    text = models.TextField(max_length=255, verbose_name='Текст вопроса')
    type = models.IntegerField(choices=QUESTION_TYPES, default=1, verbose_name='Тип вопроса')

    def __str__(self):
        return self.text


class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос на который был дан ответ')
    person_id = models.IntegerField(verbose_name='Идентификатор персоны, которая дала ответ')
    answer = models.TextField(max_length=255, verbose_name='Текст ответа')
