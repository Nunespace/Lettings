import pytest
from django.urls import reverse, resolve

from django.test import Client

client = Client()


@pytest.mark.django_db
def test_index_url():
    path = reverse("index")
    assert path == "/"
    assert resolve(path).view_name == "index"
