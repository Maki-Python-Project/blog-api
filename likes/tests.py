import pytest

from rest_framework import status


@pytest.mark.django_db
def test_like_article(api_client, user_token, article):
    url = f'/api/articles/preferences/{article["pk"]}/like/'
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token["access"]}')
    response = api_client.post(url, {})
    assert response.status_code == status.HTTP_200_OK, "Article cannot be like by user"


@pytest.mark.django_db
def test_dislike_article(api_client, user_token, article):
    url = f'/api/articles/preferences/{article["pk"]}/unlike/'
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token["access"]}')
    response = api_client.post(url, {})
    assert (
        response.status_code == status.HTTP_200_OK
    ), "Article cannot be dislike by user"
