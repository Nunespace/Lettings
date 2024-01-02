import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Letting
from pytest_django.asserts import assertTemplateUsed

client = Client()


@pytest.mark.django_db
def test_index_view(address1_fixture, address2_fixture):
    Letting.objects.create(
        title="The dream place", address=address1_fixture
    )
    Letting.objects.create(
        title="The dark place", address=address2_fixture
    )
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = '<a href="/lettings/1/">The dream place</a>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_view(address1_fixture):
    Letting.objects.create(title="The dream place", address=address1_fixture)
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = "<p>500 Dream Avenue</p>"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
