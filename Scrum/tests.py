from rest_framework.test import APITestCase
from . import views
from . models import User, Sprint, Task
from rest_framework import status
from rest_framework.reverse import reverse
# Create your tests here.


class CreateSprintTests(APITestCase):
    def setUp(self):
        pass
        # url = reverse('listcreatesprint/')
        # data = {'title': 'title'}
        # response = self.client.post(url, data, format='json')
        # return response
        # response = self.post_sprint(new_sprint_title)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Sprint.objects.count(), 1)
        # self.assertEqual(Sprint.objects.get().name, new_sprint_title)
    def test_create_sprint(self):
        url = reverse('listcreatesprint')
        data = {'title': 'title'}
        response = self.client.post(url, data, format='json')
        # return response
        # response = self.post_sprint(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sprint.objects.count(), 1)
        self.assertEqual(Sprint.objects.get().name, data)

