from django.conf.urls import url
from .api_view import (
    TaskViewSet,
    TaskDoneView
)


urlpatterns = [
    url(r'^tasks/$', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='tasks'),
    url(r'^tasks/(?P<pk>[0-9]+)/$', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
        name='single_task'),
    url(r'^tasks/status/(?P<pk>[0-9]+)/$', TaskDoneView.as_view(), name="mark_done"),
]
