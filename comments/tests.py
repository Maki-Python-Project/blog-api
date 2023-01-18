import pytest

from rest_framework import status

from comments.models import Comment
from users.models import User


@pytest.mark.django_db
def test_comments(api_client, user_token):
    url = "/api/comments/"
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token["access"]}')
    response = api_client.get(url)

    for result in response.data:

        assert Comment.objects.filter(
            text=result["text"],
            customer=User.objects.get(username=result["customer"]).pk,
        ).exists(), "Can't find comment with given data"

    assert response.status_code == status.HTTP_200_OK, "Cannot retrieve comments"
