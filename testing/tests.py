from rest_framework import test, status
from django.urls import reverse

from materials.models import Lesson
from testing.models import Question, Answers
from users.models import User


class QuestionAPITestCase(test.APITestCase):
    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.owner = User.objects.create(email="testsky@mail.pro")
        self.lesson = Lesson.objects.create(name_lesson='Тестовое занятие')
        self.question = Question.objects.create(lesson=self.lesson, question='Какой-то вопрос?')
        self.client.force_authenticate(user=self.owner)

    def test_question_list(self):
        url = reverse('testing:questions_list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question_retrueve(self):
        url = reverse('testing:question_detail', args=[self.question.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['question'], self.question.question)
        self.assertEqual(data['lesson'], self.question.lesson.pk)

