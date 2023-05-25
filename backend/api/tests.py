from http import HTTPStatus

from django.test import Client, TestCase


class TaskiApiTestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_list_exist(self):
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
