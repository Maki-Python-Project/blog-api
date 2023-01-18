from django.urls import path
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)


urlpatterns = [
    path("register/", views.RegisterApi.as_view()),
    path("logout/", views.LogoutView.as_view(), name="auth_logout"),
    path("change-password/", views.ChangePasswordView.as_view()),
]

urlpatterns += router.urls
