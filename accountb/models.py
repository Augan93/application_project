from django.db import models
from common.models import BaseModel
from django.contrib.auth.models import User


class Profile(BaseModel):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя',
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия',
    )
    confirm_id = models.CharField(
        max_length=36,
        verbose_name='ID регистрации',
    )
    confirmed = models.BooleanField(
        default=False,
        verbose_name='Email подтвержден',
    )
    confirmed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата подтверждения',
    )
    telegram_id = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Телеграм ID',
    )
    phone = models.CharField(
        max_length=20,
        default="",
        verbose_name='Телефон',
        null=True,
        blank=True,
    )
    connect_token = models.UUIDField(
        verbose_name='Токен для соединения с Телеграм ботом',
        help_text='Токен для соединения с Телеграм ботом',
        blank=True,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
