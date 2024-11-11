from django.urls import path

from rest_framework.routers import DefaultRouter

from materials.views import (CoursesViewSet, LessonCreateAPIView, LessonListAPIView,
                             LessonUpdateAPIView, LessonRetrieveAPIView, LessonDestroyAPIView)
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CoursesViewSet)

urlpatterns = [
    path('lesson/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
] + router.urls
