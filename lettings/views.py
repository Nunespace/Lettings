import logging
import sentry_sdk
from django.http import Http404
from django.shortcuts import render
from .models import Letting

logger = logging.getLogger(__name__)

# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """ Gère l'affichage d'une liste des locations sur la page lettings"""
    try:
        lettings_list = Letting.objects.all()
    except Letting.DoesNotExist:
        raise Http404("There are not lettings")
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """ Gère l'affichage du détai d'une location sur la page d'un letting"""
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        sentry_sdk.capture_message("Cette page n'existe pas", level="error")
        raise Http404("This letting does not exist")
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
