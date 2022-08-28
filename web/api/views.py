from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from dashboard.models import News
from .serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'
    search_fields = ('^text', '^title')
