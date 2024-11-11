from django.db import models

from config import settings
from materials.models import Lesson

NULLABLE = {'blank': True, 'null': True}


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Вопрос на тему')
    question = models.TextField(verbose_name='Вопрос')

    def __str__(self):
        return f'Вопрос {self.question}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural ='Вопросы'


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', **NULLABLE)
    answers = models.TextField(verbose_name='Ответ', **NULLABLE)
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ')

    def __str__(self):
        return f'Ответ {self.answers}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
