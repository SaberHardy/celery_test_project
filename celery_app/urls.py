from django.urls import path
from celery_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_mail/', views.send_email_to_all, name='send_mail'),
]
