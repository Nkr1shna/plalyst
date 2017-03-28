from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

class ExampleTestCase(APITestCase):
    def test_url_root(self):
        url = "https://www.youtube.com/watch?v=WWa4bzTJZgI"
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))