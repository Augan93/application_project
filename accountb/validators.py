from django.contrib.auth.models import User
from common.exceptions import CustomException
from django.db.models import Q
from rest_framework import status


def check_email(email):
    if User.objects.filter(Q(username=email) | Q(email=email)).exists():
        raise CustomException(key='message',
                              detail='email_duplicated',
                              status_code=status.HTTP_200_OK)
