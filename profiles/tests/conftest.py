import pytest
from profiles.models import Profile


@pytest.fixture
def user1(django_user_model):
    user = django_user_model.objects.create_user(
        username="test_user1", password="password"
    )
    return user


@pytest.fixture
def user2(django_user_model):
    user = django_user_model.objects.create_user(
        username="test_user2", password="password"
    )
    return user


@pytest.fixture
def profile1_fixture(user1):
    profile = Profile.objects.create(
        user=user1,
        favorite_city="Dream team city",
    )
    return profile


@pytest.fixture
def profile2_fixture(user2):
    profile = Profile.objects.create(
        user=user2,
        favorite_city="Dark team city",
    )
    return profile
