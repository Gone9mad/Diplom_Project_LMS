from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from materials.models import Courses, Lesson
from materials.paginators import CustomPagination
from materials.serializers import CoursesRetrieveSerializer, CoursesSerializer, LessonSerializer
from users.permissions import IsOwner, IsTeacher, IsStudents
from materials.tasks import send_mail_abount_update_materials


class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CoursesRetrieveSerializer
        return CoursesSerializer

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()

    def update(self, request, *args, **kwargs):
        courses = self.get_objects()
        serializer = self.get_serializer(courses, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def get_permissions(self):
        '''Функция которая проверяет права доступа к Эндпоинтам.'''

        if self.action == 'create':
            self.permission_classes = (IsAuthenticated | IsTeacher, ) #(AllowAny,)
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = (IsAuthenticated | IsOwner | IsTeacher | IsStudents, )
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = (IsTeacher | IsOwner, )

        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated | IsTeacher, ) #(AllowAny,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated | IsOwner | IsTeacher | IsStudents, ) #(AllowAny,)

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsTeacher | IsOwner, ) #(AllowAny,)

    def perform_update(self, serializer):
        lesson = self.get_object()
        serializer.save()
        #send_mail_abount_update_lesson.delay(lesson.sections.pk, lesson.pk)



class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated | IsOwner | IsTeacher | IsStudents, ) #(AllowAny,)


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsTeacher | IsOwner, ) #(AllowAny,)
