from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class CustomUser(User):
    age = models.PositiveIntegerField(null=True, blank=True)
