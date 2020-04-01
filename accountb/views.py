from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from . import serializers
from . import models
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        """Регистрация нового пользователя"""
        serializer = serializers.UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message": "ok"
            },
            status=status.HTTP_200_OK,
        )


class LoginView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cd = serializer.validated_data
        user = authenticate(request,
                            username=cd['username'].lower(),
                            password=cd['password'])
        if user is not None:
            refresh = RefreshToken.for_user(user)
            data = dict()
            data['refreshToken'] = str(refresh)
            data['accessToken'] = str(refresh.access_token)

            return Response(
                data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "error": "wrong_email_or_password"
                }
            )
