from rest_framework import serializers

from articles.models import Article
from comments.models import Comment
from comments.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    # comments = serializers.SerializerMethodField()

    # def get_comments(self, obj):
    #     queryset = Comment.objects.filter(article=obj.id, parent_id=None)
    #     serializer = CommentSerializer(queryset, many=True)
    #     return serializer.data

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "body",
            "category",
            "date",
            "author",
            "total_likes",
            # "comments",
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = ["id", "title", "body", "category", "date", "author"]
