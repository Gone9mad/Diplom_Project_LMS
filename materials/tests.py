from django.urls import reverse
from rest_framework import status
from rest_framework import test

from materials.models import Courses, Lesson
from users.models import User


class LessonAPITestCase(test.APITestCase):
    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.owner = User.objects.create(email="admin111@mail.ru", is_active=True)
        self.courses = Courses.objects.create(name_courses="python-develop", owner=self.owner)
        self.lesson = Lesson.objects.create(name_lesson="Algoritm", courses=self.courses, owner=self.owner)
        self.client.force_authenticate(user=self.owner)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {
            "name_lesson": "Урок_10",
            "courses": self.courses.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    '''
    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "courses": self.courses.pk,
                    "id": self.lesson.pk,
                    "name_lesson": self.lesson.name_lesson,
                    "description": self.lesson.description,
                    "preview": None,
                    "video_url": None,
                    "owner": self.owner.pk
                }
            ]
        }
        self.assertEqual(
            data, result
        )
    '''

    def test_lesson_retrieve(self):
        # Тестирование GET-запроса к API
        url = reverse('materials:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data['name_lesson'], self.lesson.name_lesson)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"name_lesson": "ООП"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name_lesson"), "ООП")

    def test_lesson_delete(self):
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )





