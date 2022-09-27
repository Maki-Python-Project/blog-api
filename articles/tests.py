import pytest


@pytest.mark.django_db
def test_capital_case():
    assert 'Semaphore' == 'Semaphore'
