from django.urls import path

from .views import index, new_parse


urlpatterns = [
    path('', index, name='index'),
    path('new_parse', new_parse, name='new_parse')
]