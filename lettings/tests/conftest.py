import pytest
from lettings.models import Address


@pytest.fixture
def address1_fixture():
    address = Address.objects.create(
        number=500,
        street="Dream Avenue",
        city="Dream city",
        state="LA",
        zip_code=10000,
        country_iso_code="USA",
    )
    return address


@pytest.fixture
def address2_fixture():
    address = Address.objects.create(
        number=300,
        street="Dark Avenue",
        city="Dark city",
        state="SF",
        zip_code=13000,
        country_iso_code="USA",
    )
    return address
