import pytest

from django.conf import settings
from rest_framework import status

from articles.models import Article


@pytest.mark.django_db
def test_create_article(api_client, user_token):
    url = settings.HOST_URL + "api/articles/"
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token["access"]}')
    response = api_client.post(url, {"title": "test article", "body": "test body"})

    assert response.status_code == status.HTTP_201_CREATED, "Cannot create article"
    assert (
        response.data["title"] == "test article"
    ), "Can't find article with given data"


@pytest.mark.django_db
def test_filter_article(api_client, article, user_token):
    url = f'/api/articles/{article["pk"]}/'
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token["access"]}')
    response = api_client.get(url)
    assert Article.objects.filter(
        title=response.data["title"]
    ), "Can't find article with given data"
    assert (
        response.status_code == status.HTTP_200_OK
    ), "Cannot retrieve specific article"


@pytest.mark.django_db
def test_article(api_client):
    url = "/api/articles/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK, "Cannot find articles"


@pytest.mark.django_db
def test_delete_article(api_client, superuser_token, article):
    url = f'/api/articles/{article["pk"]}/'
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {superuser_token["access"]}')
    response = api_client.delete(url)
    assert (
        response.status_code == status.HTTP_204_NO_CONTENT
    ), "Expected article to be deleted"
