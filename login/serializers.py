from rest_framework import serializers
from django.core.validators import EmailValidator
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[EmailValidator()])
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Email and password are required")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        user = authenticate(username=user.username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")

        attrs["user"] = user
        return attrs

    class Meta:
        model = User
        fields = ["email", "password"]
