from django.urls import path
from . import views


app_name = 'apps'

urlpatterns = [
    path('applications/create/', views.ApplicationCreateView.as_view(), name='applications-create'),
    path('applications/', views.ApplicationRetrieveView.as_view(), name='applications-retrieve'),
    path('applications/edit/', views.ApplicationEditView.as_view(), name='applications-update'),
    path('applications/delete/', views.ApplicationDeleteView.as_view(), name='applications-delete'),
]
