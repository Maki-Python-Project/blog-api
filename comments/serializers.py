from rest_framework import serializers

from comments.models import Comment


class FilterCommentListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source="customer.username")
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ["text", "article", "customer", "published", "children"]
