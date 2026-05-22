from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_notification, name='test_notification'),
]