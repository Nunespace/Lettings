import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


client = Client()

@pytest.mark.django_db
def test_index_view(profile1_fixture, profile2_fixture):
    profile1 = profile1_fixture
    profile2 = profile2_fixture
    path = reverse("profiles:index")
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = '<a href="/profiles/test_user2/">test_user2</a>'
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")



@pytest.mark.django_db
def test_profile_view(profile1_fixture):
    profile = profile1_fixture
    path = reverse("profiles:profile", kwargs={"username": "test_user1"})
    response = client.get(path)
    content = response.content.decode()
    print("content : ", content)
    expected_content = "Dream team city"
    assert expected_content in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
