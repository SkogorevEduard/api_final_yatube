from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Класс получения разрешения на изменения объекта'''
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        '''Метод проверки пользовательского разрешения.'''
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)
