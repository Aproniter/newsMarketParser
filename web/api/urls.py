from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import NewsViewSet


app_name = 'api'

router = SimpleRouter()
router.register('^news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]