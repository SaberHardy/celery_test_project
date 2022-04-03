from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from celery_app.tasks import test_func


def home(request):
    test_func.delay()
    return HttpResponse("Done")
