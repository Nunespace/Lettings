from django.shortcuts import render
from .models import Profile


def index(request):
    """Renvoie vers la page affichant la liste des profils des clients"""
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Renvoie vers la page détaillant un profil"""
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
