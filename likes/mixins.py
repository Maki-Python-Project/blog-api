from rest_framework.decorators import action
from rest_framework.response import Response

from . import services
from .serializers import FanSerializer
from users.models import User


class LikedMixin:
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        obj = self.get_object()
        user = User.objects.get(id=request.user.id)
        services.add_like(obj, user)

        return Response()

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        user = User.objects.get(id=request.user.id)
        services.remove_like(obj, user)

        return Response()

    @action(detail=True, methods=['get'])
    def get_fans(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)

        return Response(serializer.data)
