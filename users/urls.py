from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterApi.as_view()),
    path('logout/', views.LogoutView.as_view(), name='auth_logout'),
]
