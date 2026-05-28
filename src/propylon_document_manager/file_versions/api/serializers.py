from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import FileVersion

User = get_user_model()


class FileVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileVersion
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "name", "password"]

    def create(self, validated_data: dict):
        """Create a new user instance from validated registration data.

        Args:
            validated_data (dict): The validated data from the serializer,
                containing user credentials such as name, email and password.

        Returns:
            User: A new user object created with the provided name, email and password.
        """
        return User.objects.create_user(
            name=validated_data["name"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
