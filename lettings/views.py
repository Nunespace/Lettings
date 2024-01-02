import logging
import sentry_sdk
from django.http import Http404
from django.shortcuts import render
from .models import Letting

# le nom du logger se rapporte à la hiérarchie du paquet et des modules,
# on peut ainsi voir où un événement a été enregistré simplement en regardant
# le nom du logger: en cas d'erreur, le logger ici sera lettings.views
logger = logging.getLogger(__name__)


def index(request):
    """Gère l'affichage d'une liste des locations sur la page lettings"""
    try:
        lettings_list = Letting.objects.all()
    except Letting.DoesNotExist:
        raise Http404("There are not lettings")
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Gère l'affichage du détail d'une location sur la page d'une location (letting)
    Retourne une page letting ou la page personnalisée 404 en cas d'erreur d'id
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        sentry_sdk.capture_message("Cette page n'existe pas", level="error")
        logger.error("Cette page n'existe pas")
        raise Http404("This letting does not exist")
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
