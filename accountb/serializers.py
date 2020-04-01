from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from .validators import check_email
from uuid import uuid4


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
    )
    email = serializers.EmailField(
        required=True,
    )
    firstName = serializers.CharField(
        max_length=100,
        required=True,
    )
    lastName = serializers.CharField(
        max_length=100,
        required=True,
    )
    phone = serializers.CharField(
        max_length=20,
        allow_blank=True,
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'password',
            'password2',
            'email',
            'firstName',
            'lastName',
            'phone',
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {
                    "Error": "Пароли не совпадают"
                }
            )
        # password2 = data['password2']
        # password_validation.validate_password(password2)
        check_email(data['email'])

        return data

    def create(self, validated_data):
        email = validated_data['email'].lower()
        user = User(
            username=email,
            email=email,
        )
        user.set_password(validated_data['password'])
        user.save()
        models.Profile.objects.create(
            user=user,
            first_name=validated_data['firstName'],
            last_name=validated_data['lastName'],
            phone=validated_data.get('phone'),
            confirm_id=str(uuid4()),
            connect_token=str(uuid4()),
            confirmed=True  # Для теста
        )

        # send_confirm_url.delay(user.id)  # Задача для Celery

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        required=True,
    )


class ProfileDetailSerializer(serializers.ModelSerializer):
    userId = serializers.PrimaryKeyRelatedField(
        source='user',
        read_only=True,
    )
    firstName = serializers.CharField(
        max_length=100,
        source='first_name',
        required=True,
    )
    lastName = serializers.CharField(
        max_length=100,
        source='last_name',
        required=True,
    )

    class Meta:
        model = models.Profile
        fields = (
            'userId',
            'firstName',
            'lastName',
        )

