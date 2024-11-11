from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializers


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        if user.role == 'teacher':
            group = Group.objects.get(name='teacher')
            group.user_set.add(user)
        elif user.role == 'student':
            group = Group.objects.get(name='student')
            group.user_set.add(user)
        user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsOwner, )


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializers
    permission_classes = (IsOwner, )
