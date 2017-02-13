from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN
)

from todo.models import (
    Task,
    Log
)


class ApiTest(TestCase):

    def setUp(self):
        self.username1 = 'test'
        self.username2 = 'test2'
        self.pass1 = 'Testpass1'
        self.pass2 = 'Testpass2'
        u1 = User.objects.create(username=self.username1)
        u1.set_password(self.pass1)
        u1.save()
        u2 = User.objects.create(username=self.username2)
        u2.set_password(self.pass2)
        u2.save()
        self.client = APIClient()
        self.tasks_url = reverse('tasks')

    def test_permission(self):
        self.client.login(username=self.username1, password=self.pass1)
        # test create view
        response = self.client.post(self.tasks_url, data={'name': 'test', 'description': 'description'})
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        task_pk = Task.objects.first().pk
        single_task_url = reverse('single_task', kwargs={'pk': task_pk})
        self.client.login(username=self.username2, password=self.pass2)

        # trying to update another user task
        response = self.client.put(single_task_url, data={'name': 'test', 'description': 'description'})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

        # change status of another user task
        status_url = reverse('mark_done', kwargs={'pk': task_pk})
        response = self.client.put(status_url, data={'status': True})

        self.assertEqual(response.status_code, HTTP_200_OK)

        task = Task.objects.first()
        self.assertTrue(task.status)

        # check that log created
        self.assertEquals(task.logs.count(), 1)

        log = task.logs.first()

        self.assertEquals(log.user.username, self.username2)
