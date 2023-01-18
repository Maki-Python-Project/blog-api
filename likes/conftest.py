import pytest

from datetime import datetime
from rest_framework.test import APIClient
from django.urls import reverse

from articles.models import Article
from users.models import User
from users.serializers import UserSerializer


@pytest.fixture
def author_data():
    return {"username": "Itan", "email": "itan@email.com", "password": "12341234q"}


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_data(db):
    user_info = {
        "username": "user",
        "email": "user@email.com",
        "password": "P@ssw0rd4321",
    }
    user = User.objects.create_user(**user_info)
    user_data = UserSerializer(user).data
    user_data["password"] = user_info["password"]
    return user_data


@pytest.fixture
def user_token(api_client, user_data):
    url = reverse("token_obtain_pair")
    response = api_client.post(
        url,
        {"username": user_data["username"], "password": user_data["password"]},
        format="json",
    )
    return response.data


@pytest.fixture
def article(author_data):
    author = User(**author_data)
    author.save()

    article_data = {
        "pk": 1,
        "title": "test title",
        "body": "test body",
        "author": author,
        "date": datetime.now(),
    }
    article = Article(**article_data)
    article.save()

    return article_data
