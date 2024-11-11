from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    '''
        Права доступа для пользователей, которые являются владельцами контента.
    '''
    def has_object_permission(self, request, view, obj):
        if obj.owner in request.user:
            return True
        return False


class IsTeacher(permissions.BasePermission):
    '''
        Функция кастомных прав доступа,
        которая проверяет входит ли users в состав group.teacher.
    '''

    def has_permission(self, request, view):
        if request.user.groups.filter(name='teacher').exists():
            return True


class IsStudents(permissions.BasePermission):
    '''
        Функция кастомных прав доступа,
        которая проверяет входит ли users в состав group.students.
    '''
    def has_permission(self, request, view):
        return request.user.groups.filter(name='students').exists()
