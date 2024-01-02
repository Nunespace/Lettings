import pytest

from django.test import Client
from profiles.models import Profile

client = Client()


@pytest.mark.django_db
def test_profile_model(user1):
    profile = Profile.objects.create(
        user=user1,
        favorite_city="Very big city",
    )
    expected_value = "test_user1"
    assert str(profile) == expected_value
