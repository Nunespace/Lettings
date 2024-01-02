import pytest
from django.urls import reverse, resolve

from django.test import Client

client = Client()


@pytest.mark.django_db
def test_index_url(profile1_fixture, profile2_fixture):
    profile1_fixture
    profile2_fixture
    path = reverse("profiles:index")
    assert path == "/profiles/"
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_url(profile1_fixture):
    profile1_fixture
    path = reverse("profiles:profile", kwargs={"username": "test_user1"})

    assert path == "/profiles/test_user1/"
    assert resolve(path).view_name == "profiles:profile"
