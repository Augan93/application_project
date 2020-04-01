from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from . import permissions


class ApplicationCreateView(generics.CreateAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer


class ApplicationEditView(generics.UpdateAPIView):
    permission_classes = (
        IsAuthenticated,
        permissions.ApplicationOwnerPermission,
    )
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

    def update(self, request, *args, **kwargs):
        api_key = request.query_params.get('api_key')

        try:
            app = models.Application.objects.get(api_key=api_key,
                                                 is_active=True)
        except models.Application.DoesNotExist:
            return Response(
                {
                    'message': 'not_found',
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        self.check_object_permissions(request, app)
        serializer = self.serializer_class(data=request.data,
                                           instance=app)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class ApplicationRetrieveView(generics.RetrieveAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

    def get(self, request, *args, **kwargs):
        api_key = request.query_params.get('api_key')

        try:
            app = models.Application.objects.get(api_key=api_key,
                                                 is_active=True)
        except models.Application.DoesNotExist:
            return Response(
                {
                    'message': 'not_found',
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(instance=app)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )


class ApplicationDeleteView(generics.RetrieveAPIView):
    permission_classes = (
        IsAuthenticated,
        permissions.ApplicationOwnerPermission,
    )
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

    def delete(self, request, *args, **kwargs):
        api_key = request.query_params.get('api_key')

        try:
            app = models.Application.objects.get(api_key=api_key,
                                                 is_active=True)
        except models.Application.DoesNotExist:
            return Response(
                {
                    'message': 'not_found',
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        self.check_object_permissions(request, app)
        app.is_active = False
        app.save()

        return Response(
            {
                'message': 'ok',
            },
            status=status.HTTP_204_NO_CONTENT
        )

