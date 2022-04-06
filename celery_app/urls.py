from django.urls import path
from celery_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_mail/', views.send_email_to_all, name='send_mail'),
    path('program_mail/', views.send_mail_at_particular_time, name='program_mail'),
]
