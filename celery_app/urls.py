from django.urls import path
from celery_app import views

urlpatterns = [
    path('', views.home, name='home'),
]
