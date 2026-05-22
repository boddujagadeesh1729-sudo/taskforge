from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def test_notification(request):
    return HttpResponse("Notification test")
