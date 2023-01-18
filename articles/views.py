from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from articles.serializers import ArticleSerializer, ArticleDetailSerializer
from articles.models import Article
from articles.permissions import AdminOrAccountOwnerPermission
from articles.filters import ArticleFilter
from likes.mixins import LikedMixin


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10


class ArticleViewSet(LikedMixin, viewsets.ModelViewSet):
    filterset_class = ArticleFilter
    pagination_class = StandardResultsSetPagination

    filter_backends = [
        DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter
    ]

    filterset_fields = ['title']
    search_fields = ['title', 'body']
    ordering_fields = ['id']

    permission_classes_by_action = {
        'update': [AdminOrAccountOwnerPermission, IsAuthenticated],
        'create': [IsAuthenticated],
        'destroy': [AdminOrAccountOwnerPermission, IsAuthenticated],
        'partial_update': [AdminOrAccountOwnerPermission, IsAuthenticated]
    }

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        return Article.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return ArticleSerializer
        elif self.action in ['retrieve', 'delete', 'update', 'partial_update']:
            return ArticleDetailSerializer


class LikeViewSet(LikedMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
