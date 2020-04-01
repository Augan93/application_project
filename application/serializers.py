from rest_framework import serializers
from . import models


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = (
            'id',
            'name',
            'description',
            'api_key',
            'is_active',
            'owner',
            'created',
        )
        read_only_fields = (
            'api_key',
            'is_active',
            'created',
            'owner',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        return models.Application.objects.create(
            owner=request.user,
            **validated_data
        )
