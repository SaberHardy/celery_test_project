from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from send_email.tasks import send_mail_func
from celery_app.tasks import test_func


def home(request):
    test_func.delay()
    return HttpResponse("Done")


def send_email_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Successfully sent")
