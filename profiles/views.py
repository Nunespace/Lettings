import logging
import sentry_sdk
from django.http import Http404
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Renvoie vers la page affichant la liste des profils des clients"""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """
    Renvoie vers la page détaillant un profil ou vers une page
    personnalisée 404 en cas de nom de profil inexistant
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        sentry_sdk.capture_message("Cette page n'existe pas!", level="error")
        logger.error("Cette page n'existe pas")
        raise Http404("This profile does not exist")
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
