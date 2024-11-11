from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Courses(models.Model):
    '''
        Модель Курсы(Разделы)
    '''
    name_courses = models.CharField(max_length=100, verbose_name='Название курса')
    preview = models.ImageField(upload_to='materials/preview', verbose_name='Изображение', **NULLABLE)
    description = models.TextField(verbose_name='Описание курса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name_courses

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    '''
        Модель Уроки(Материалы)
    '''
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    name_lesson = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание урока', **NULLABLE)
    preview = models.ImageField(upload_to='materials/preview', verbose_name='Изображение', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name_lesson

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
