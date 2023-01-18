from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from comments.filter import CommentFilter
from comments.serializers import CommentSerializer
from comments.permissions import AdminOrAccountOwnerPermission


class CommentList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all().select_related('customer')
    serializer_class = CommentSerializer
    filterset_class = CommentFilter

    def perform_create(self, serializer: CommentSerializer) -> None:
        serializer.save(
            customer=self.request.user
        )


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    filterset_class = CommentFilter
    serializer_class = CommentSerializer

    def get_permissions(self) -> permissions.BasePermission:
        if self.request.method not in permissions.SAFE_METHODS:
            return [AdminOrAccountOwnerPermission(), IsAuthenticated()]
        return [IsAuthenticated()]
