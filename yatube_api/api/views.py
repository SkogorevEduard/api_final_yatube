from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from .permissions import IsAuthorOrReadOnly

from posts.models import Group, Post, Comment, Follow

from .serializers import (
    GroupSerializer,
    PostSerializer,
    CommentSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    '''Вьюсет для работы с моделью Post.'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        '''Метод создания поста.'''
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''Вьюсет для работы с моделью Group.'''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    '''Вьюсет для работы с моделью Comment.'''
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        '''Метод создания комментария.'''
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs.get("post_id"))
        )

    def get_queryset(self):
        '''Метод получения всех комментариев поста.'''
        post_id = self.kwargs.get("post_id")
        queryset = Comment.objects.filter(post=post_id)
        return queryset


class FollowViewSet(viewsets.ModelViewSet):
    '''Вьюсет для работы с моделью Follow.'''
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        '''Метод подписки.'''
        serializer.save(user=self.request.user)

    def get_queryset(self):
        '''Метод получения всех подписок.'''
        return Follow.objects.filter(user=self.request.user)
