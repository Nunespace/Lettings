import pytest
from django.urls import reverse, resolve
from lettings.models import Letting
from django.test import Client

client = Client()


@pytest.mark.django_db
def test_index_url(address1_fixture, address2_fixture):
    Letting.objects.create(
        title="The dream place", address=address1_fixture
    )
    Letting.objects.create(
        title="The dark place", address=address2_fixture
    )
    path = reverse("lettings:index")
    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"


@pytest.mark.django_db
def test_letting_url(address1_fixture):
    Letting.objects.create(title="The dream place", address=address1_fixture)
    path = reverse("lettings:letting", kwargs={"letting_id": 1})

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"
