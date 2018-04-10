from django.test import TestCase, Client
from posts.models import *
from posts.views import *
import requests
import unittest

#empty home view
class EmptyHomepageTestCase(TestCase):

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


#filled homepage view
class FilledHomepageTestCase(TestCase):

    #setup to have populated homepage
    def setUp(self):

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

    #get from populated homepage
    def test_homepage_get_normal(self):

        c = Client()

        response = c.get('/api/home/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'result': {'3': {'author_id': 3, 'date': '2018-03-26T01:03:13.178Z', 'description': 'test', 'id': 3, 'location': 'test', 'part': 'test', 'payment_method': 'test', 'price': 0.0, 'title': 'test', 'transaction_type': 'Buying'}}, 'status': True}
        )

    #post from populated homepage
    def test_homepage_post_normal(self):

        c = Client()

        response = c.post('/api/home/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'Nothing to POST'}
        )

    #teardown
    def teardown(self):
        p.delete()
        u.delete()



#post_detail view empty
class EmptyDetailTestCase(TestCase):

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



#filled post_detail view
class FilledDetailTestCase(TestCase):

    def setUp(self):

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


    #get request on non-empty detail page
    def test_detail_get_stuff(self):

        c = Client()

        response = c.get('/api/post_detail/1')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'author': 1, 'date': '2018-03-26T01:03:13.178Z', 'description': 'test', 'id': 1, 'location': 'test', 'part': 'test', 'payment_method': 'test', 'price': 0.0, 'transaction_type': 'Buying', 'title': 'test'}
        )

    #post request on non-empty detail page
    def test_detail_post_stuff(self):

        c = Client()

        response = c.post('/api/post_detail/1')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'nothing to POST, only viewing a post detail'}
        )

    def teardown(self):
        p.delete()
        u.delete()



#not authenticated check_auth view
class NotCheckAuthTestCase(TestCase):


    #get when auth doesnt exist
    def test_checkauth_get_noauth(self):

        c = Client()

        response = c.get('/api/check_auth')

        self.assertEqual(response.status_code, 301)

    #post when auth doesnt exist
    def test_checkauth_post_noauth(self):

        c = Client()

        response = c.post('/api/check_auth')
        self.assertEqual(response.status_code, 301)
        # self.assertJSONEqual(
        #     str(response.content, encoding='utf8'),
        #     {'status': False}
        # )



#authenticated check_auth view
class YesCheckAuthTestCase(TestCase):

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


    #post when auth exists
    def test_checkauth_post_auth(self):

        c = Client()

        response = c.post('/api/check_auth')

        self.assertEqual(response.status_code, 301)
        # self.assertJSONEqual(
        #     str(response.content, encoding='utf8'),
        #     {'status': True}
        # )

    def teardown(self):
        a.delete()



#when logged out add_post view
class OutAddPostTestCase(TestCase):

    #get when logged out
    def test_add_get_out(self):

        c = Client()

        response = c.get('/api/add_post/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': True, 'result': 'Get'}
        )


    #post when logged out
    def test_add_post_out(self):

        c = Client()

        response = c.post('/api/add_post/')



#when logged in add_post view
class InAddPostTestCase(TestCase):

    #setup to be logged in 


    #get when logged in
    def test_add_get_in(self):

        c = Client()

        response = c.get('/api/add_post/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': True, 'result': 'Get'}
        )


    #post when logged in
    def test_add_post_in(self):

        c = Client()

        response = c.post('/api/add_post/')




# not registered register view
class NotRegisterTestCase(TestCase):

    #get when not registered
    def test_register_get_notregistered(self):

        c = Client()

        response = c.get('/api/register/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Error, cannot complete GET request")

    #post when not registered
    def test_register_post_notregistered(self):
        
        c = Client()

        # response = c.post('/api/register/')



# not registered register view
class YesRegisterTestCase(TestCase):

    # #setup to register user
    # def setup(self):



    #get when registered
    def test_register_get_registered(self):

        c = Client()

        response = c.get('/api/register/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Error, cannot complete GET request")

    #post when registered
    def test_register_post_registered(self):

        c = Client()

        # response = c.post('/api/register/')



#logged out login view
class OutLoginTestCase(TestCase):

    #get when logged out
    def test_login_get_logged_out(self):

        c = Client()

        response = c.get('/api/login/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Error, cannot complete GET request")

    #post when logged out
    def test_login_post_logged_out(self):

        c = Client()

        # response = c.post('/api/login/')



#logged in login view
class InLoginTestCase(TestCase):

    # #setup to be logged in
    # def setup(self):


    #get when logged in
    def test_login_get_logged_out(self):

        c = Client()

        response = c.get('/api/login/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Error, cannot complete GET request")

    #post when logged out
    def test_login_post_logged_out(self):

        c = Client()

        # response = c.post('/api/login/')





# logged out logout view
class OutLogoutTestCase(TestCase):

    #get when logged out
    def test_logout_get_logged_out(self):

        c = Client()

        response = c.get('/api/logout/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Error, cannot complete GET request")

    #post when logged out
    def test_logout_post_logged_out(self):

        c = Client()

        # response = c.post('/api/logout/')

        # self.assertEqual(response.status_code, 200)
        # self.assertJSONEqual(
        #     str(response.content, encoding='utf8'),
        #     {'status': False, 'result': 'User is not logged in'}
        # )


#logged in login view
class InLogoutTestCase(TestCase):

    # #setup logging in 
    def setUp(self):

        a = Authenticator(
            auth = 'test',
            date_created = '2018-03-26T01:03:13.178Z',
            user_id = 1)
        a.save()

    #get when logged in
    def test_logout_get_logged_in(self):

        c = Client()

        response = c.get('/api/logout/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode('utf-8'), "Error, cannot complete GET request")

    #post when logged in
    def test_logout_post_logged_in(self):

        c = Client()

        # response = c.post('/api/logout/')

        # self.assertEqual(response.status_code, 200)
        # self.assertJSONEqual(
        #     str(response.content, encoding='utf8'), 
        #     {'status': True, 'result': 'You have successfully logged out'}
        # )

    def teardown(self):

        a.delete()


