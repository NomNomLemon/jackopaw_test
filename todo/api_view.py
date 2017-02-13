from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import (
    Task,
    Log
)
from .perimissions import OwnTaskPermission
from .serializers import (
    TaskPostSerializer,
    TaskGetSerializer,
    TaskDoneSerializer,
)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskGetSerializer
    serializer_class_post = TaskPostSerializer
    permission_classes = (OwnTaskPermission, IsAuthenticated)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return self.serializer_class_post
        else:
            return self.serializer_class


class TaskDoneView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDoneSerializer

    def put(self, request, *args, **kwargs):
        response = super().put(request, args, kwargs)
        instance = self.get_object()
        Log.objects.create(task=instance, user=request.user, action='Set status to {}'.format(instance.status_display))
        return response
