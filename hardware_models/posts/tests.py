from django.test import TestCase, Client
from posts.models import *
from posts.views import *
import requests
import unittest

#home view
class HomepageTestCase(TestCase):


    #get from empty homepage 
    def test_homepage_get_empty(self):

        c = Client()

        response = c.get('/api/home/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'result': {}, 'status': True}
        )

    #post from empty homepage
    def test_homepage_post_empty(self):

        c = Client()

        response = c.post('/api/home/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'Nothing to POST'}
        )

    #get from populated homepage
    def test_homepage_get_normal(self):

        u = Profile(
            display_name='Tester',
            email='tester@test.com',
            password='Test',
            username='Tester')
        u.save()

        p = Post.objects.create(
            author=u,
            date='2018-03-26T01:03:13.178Z',
            description='test',
            location='test',
            part='test',
            payment_method='test',
            price=0.0,
            transaction_type='Buying',
            title='test')
        p.save()

        c = Client()

        response = c.get('/api/home/')

        self.assertEqual(response.status_code, 200)
        # self.assertJSONEqual(
        #     str(response.content, encoding='utf8'),
        #     {'result': {'1': {'author': 'Tester', 'date': '2018-03-26T01:03:13.178Z', 'description': 'test', 'location': 'test', 'part': 'test', 'payment_method': 'test', 'price': 0.0, 'transaction_type': 'test', 'title': 'test'}}, 'status': True}
        # )


    #post from populated homepage
    def test_homepage_post_normal(self):

        c = Client()

        response = c.post('/api/home/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'Nothing to POST'}
        )


#post_detail view
class DetailTestCase(TestCase):

    def setup(self):

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

    #get request on non-empty detail page
    def test_detail_get_stuff(self):

        c = Client()

        response = c.get('/api/post_detail/1')

        self.assertEqual(response.status_code, 200)
        ##########stuff to test response page?????????##############

    #post request on non-empty detail page
    def test_detail_post_stuff(self):

        c = Client()

        response = c.post('/api/post_detail/1')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'nothing to POST, only viewing a post detail'}
        )

    #get request on empty detail page
    def test_detail_get_empty(self):

        c = Client()

        response = c.get('/api/post_detail/2')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'error': 'object does not exist'}
        )

    #post request on empty detail page 
    def test_detail_post_empty(self):

        c = Client()

        response = c.post('/api/post_detail/2')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'nothing to POST, only viewing a post detail'}
        )


#check_auth view
class CheckAuthTestCase(TestCase):


    #get when auth doesnt exist
    def test_checkauth_get_noauth(self):

        c = Client()

        response = c.get('/api/check_auth')

        self.assertEqual(response.status_code, 301)
        # self.assertEqual(response.content, "Error, cannot complete GET request")

    #post when auth doesnt exist
    def test_checkauth_post_noauth(self):

        c = Client()

        response = c.post('/api/check_auth')
        self.assertEqual(response.status_code, 301)
        # self.assertJSONEqual(
        #     str(response.content, encoding='utf8'),
        #     {'status': False}
        # )


    #create an authenticator
    def setUp(self):

        a = Authenticator(
            auth = 'test',
            date_created = '2018-03-26T01:03:13.178Z',
            user_id = 1)
        a.save()

    #get when auth exists
    def test_checkauth_get_auth(self):

        c = Client()

        response = c.get('/api/check_auth')

        self.assertEqual(response.status_code, 301)
        # self.assertEqual(response.content, "Error, cannot complete GET request")


    #post when auth exists
    def test_checkauth_post_auth(self):

        c = Client()

        response = c.post('/api/check_auth')

        self.assertEqual(response.status_code, 301)
        # self.assertJSONEqual(
        #     str(response.content, encoding='utf8'),
        #     {'status': True}
        # )



# #add_post view
# class AddPostTestCase(TestCase):

#     c = Client()

#     #get request
#     response = c.get('/api/home/')
#     self.assertJSONEqual(
#         str(response.content, encoding='utf8'),
#         {'result': {}, 'status': True}
#     )

#     #post request 
#     response = c.post('/api/home/')
#     self.assertJSONEqual(
#         str(response.content, encoding='utf8'),
#         {'status': 'Nothing to POST'}
#     )


# #register view
# class RegisterTestCase(TestCase):



# #login view
# class LoginTestCase(TestCase):



# #create_authenticator view
# class CreateAuthTestCase(TestCase):



# #logout view
# class LogoutTestCase(TestCase):

#     #get when logged out
#     def test_logout_get_logged_out(self):

#         c = Client()

#         response = c.get('/api/logout/')

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content, "Error, cannot complete GET request")

#     #post when logged out
#     def test_logout_post_logged_out(self):

#         c = Client()

#         response = c.post('/api/logout/')

#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(
#             str(response.content, encoding='utf8'),
#             {'status': False, 'result': 'User is not logged in'}
#         )

#     #setup logging in 
#     def setUp(self):

#         c = Client()




#     #get when logged in
#     def test_logout_get_logged_in(self):

#         response = c.get('/api/logout/')

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content, "Error, cannot complete GET request")

#     #post when logged in
#     def test_logout_post_logged_in(self):

#         response = c.post('/api/logout/')

#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(
#             str(response.content, encoding='utf8'), 
#             {'status': True, 'result': 'You have successfully logged out'}
#         )


