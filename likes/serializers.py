from rest_framework import serializers

from users.models import User


class FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()
