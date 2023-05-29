from rest_framework import serializers

from umravaxajapp.models import AdminUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = "__all__"
