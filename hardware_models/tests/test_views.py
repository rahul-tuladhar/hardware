from django.test import TestCase
from posts.views import *
import requests
import unittest


class ModelsLayerTestCase(TestCase):
    def test_homepage_get(self):
        request = 'GET'
        response = home(request)
        self.assertEqual(response.status_code, 200)
