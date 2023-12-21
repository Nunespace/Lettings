from django.shortcuts import render
from sentry_sdk import capture_message


def index(request):
    """ Renvoie la page d'accueil"""
    return render(request, 'index.html')


def handler404(request, exception):
    capture_message("Page not found!", level="error")
    return render(request, '404.html', status=404)


def handler500(request):
    capture_message("Profile not found!", level="error")
    return render(request, '500.html', status=500)
