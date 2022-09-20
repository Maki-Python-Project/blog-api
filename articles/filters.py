from django_filters import rest_framework as filters

from articles.models import Article


class ArticleFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='iexact')
    author = filters.CharFilter(field_name='author__username', lookup_expr='iexact')

    class Meta:
        model = Article
        fields = ['id', 'title', 'author']
