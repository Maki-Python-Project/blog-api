import pytest

from .models import Article


@pytest.mark.django_db
def test_capital_case():
    qs = Article.objects.filter(id=1)
    assert qs.title == 'qq'
