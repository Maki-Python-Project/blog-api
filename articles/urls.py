from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'preferences', views.LikeViewSet)


urlpatterns = format_suffix_patterns([
    path('', views.ArticleViewSet.as_view({
        'get': 'list', 'post': 'create'
        })
    ),
    path('<int:pk>/', views.ArticleViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy',
            'patch': 'partial_update'
        })
    ),
])

urlpatterns += router.urls
