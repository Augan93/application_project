from django.db import models
from common.models import BaseModel
from uuid import uuid4
from django.contrib.auth import get_user_model

User = get_user_model()


class Application(BaseModel):
    name = models.CharField(
        max_length=500,
        verbose_name='Название',
    )
    api_key = models.CharField(
        max_length=50,
        verbose_name='Ключ API',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET(get_user_model),
        related_name='my_cars',
        verbose_name='Хозяин',
    )
    description = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
    )

    @staticmethod
    def generate_api_key():
        return str(uuid4())

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding:
            """При создании генерируем api_key"""
            self.api_key = self.generate_api_key()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'

