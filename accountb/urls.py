from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

app_name = 'accountb'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('authenticate/', views.LoginView.as_view(), name='login'),
]
