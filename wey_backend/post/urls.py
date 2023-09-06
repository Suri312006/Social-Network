from django.urls import path, include

from . import api

urlpatterns = [
    path('', api.post_list, name='post list'),
    path('create/', api.post_create, name='post_create')
]