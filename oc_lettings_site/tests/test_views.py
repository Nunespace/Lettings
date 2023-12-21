import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_index_view():
    path = reverse("index")
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = '<h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "index.html")

"""
@pytest.mark.django_db
def test_handler404_view():
    path = reverse("lettings:letting", kwargs={"letting_id": 999})
    response = client.get(path)
    assert response.status_code == 404
"""
