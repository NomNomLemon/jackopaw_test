from rest_framework import serializers
from .models import Task, Log, User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = ['id', 'name']


class LogSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Log
        fields = ['user', 'action']


class TaskDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']


class TaskPostSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Task
        fields = ['name', 'description', 'status']

    def save(self, **kwargs):
        self.validated_data['user'] = self.context['request'].user
        return super().save()


class TaskGetSerializer(TaskPostSerializer):
    user = UserSerializer()
    logs = LogSerializer(many=True)

    class Meta:
        model = Task
        fields = ['id', 'user', 'name', 'description', 'status', 'logs']
