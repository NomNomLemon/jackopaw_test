from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class DateTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Task(DateTracking, models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256)
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return 'user {}, task: {}, status: {}'.format(self.user.get_full_name(), self.name, self.status_display)

    @property
    def status_display(self):
        return 'Done' if self.status else 'Undone'


class Log(DateTracking, models.Model):
    user = models.ForeignKey(User, related_name='actions')
    task = models.ForeignKey(Task, related_name='logs')
    action = models.TextField()

    def __str__(self):
        return 'user {}, task: {}, action: {}'.format(self.user.get_full_name(), self.task.name, self.action)
