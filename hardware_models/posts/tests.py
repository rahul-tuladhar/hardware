from django.test import TestCase, Client
from posts.models import *
from posts.views import *
import requests
import unittest


class HomepageTestCase(TestCase):
    def test_homepage(self):
        c = Client()
        response = c.get('/api/home/')
        self.assertEqual(response.status_code, 200)
        response = c.post('/api/home/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_no_posts(self):
        c = Client()
        response = c.get('/api/home/')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'result': {}, 'status': True}
        )
        response = c.post('/api/home/')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'Nothing to POST'}
        )


class DetailTestCase(TestCase):
    def test_detail_page(self):
        u = Profile(
            display_name='Tester',
            email='tester@test.com',
            password='Test',
            username='Tester'
        )
        u.save()
        p = Post(
            author=u,
            date='2018-03-26T01:03:13.178Z',
            description='Descirption',
            location='location',
            part='Computer',
            payment_method='cash',
            price=10.0,
            transaction_type='Buying',
            title='first',
        )
        p.save()
        c = Client()
        response = c.get('/api/post_detail/1')
        self.assertEqual(response.status_code, 200)
        response = c.get('/api/post_detail/2')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'error': 'object does not exist'}
        )
        response = c.post('/api/post_detail/1')
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'nothing to POST, only viewing a post detail'}
        )
