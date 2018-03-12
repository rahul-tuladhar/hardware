from django.test import TestCase
from django.core.urlresolvers import reverse


class LoginViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    # def success_response(self):
    #        #assumes user with id 1 is stored in db
    #        response = self.client.get(reverse('all_orders_list', kwargs={'user_id':1}))

    #        #checks that response contains parameter order list & implicitly
    #        # checks that the HTTP status code is 200
    #        self.assertContains(response, 'order_list')

    #        #user_id not given in url, so error
    #    def fails_invalid(self):
    #        response = self.client.get(reverse('all_orders_list'))
    #        self.assertEquals(response.status_code, 404)

    def tearDownTestData(cls):
        pass


class PostViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    # test cases for the experience layer api
    def test_homepage_template(self):
        """ Tests whether the correct homepage template is used """
        r = self.client.get(reverse('homepage'))
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed(r, 'hardware_models/homepage.html')

    def test_homepage_is_paginated(self):
        """ Tests whether the homepage is paginated (as it should be) """
        r = self.client.get(reverse('homepage'))
        self.assertEquals('is_paginated' in r.context)
        self.assertTrue(r.context['is_paginated'] is True)
        self.assertTrue(len(r.context['post_list']) == 3)  # assumes we are going to have 3 posts as an example

    def test_list_all_posts(self):
        """ Tests whether all posts is listed correctly """
        r = self.client.get(reverse('index'))
        self.assertEquals(r.status_code, 200)


    def tearDownTestData(cls):
        pass


class ReviewViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def tearDownTestData(cls):
        pass
