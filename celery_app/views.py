from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from send_email.tasks import send_mail_func
from celery_app.tasks import test_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


def home(request):
    test_func.delay()
    return HttpResponse("Done")


def send_email_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Successfully sent")


def send_mail_at_particular_time(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=19, minute=16)
    task = PeriodicTask.objects.create(crontab=schedule,
                                       name='schedule_mail_task_' + '5',
                                       task='send_email.tasks.send_mail_func',
                                       # args=json.dumps(([2, 3]))
                                       )
    return HttpResponse("send_mail_at_particular_time Successfully sent")
