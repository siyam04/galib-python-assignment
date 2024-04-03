from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model
    """
    name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'name', 'phone', 'password', 'email')
        extra_kwargs = {
            'username': {"write_only": True},
            'first_name': {'required': True, "write_only": True},
            'last_name': {'required': True, "write_only": True},
            'email': {'required': True},
            'phone': {'required': True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def get_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
