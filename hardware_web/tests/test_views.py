from django.test import TestCase
from django.core.urlresolvers import reverse


class PostViewTest(TestCase):
    """ Tests the views for login """

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        :return: None
        """

    def test_homepage_template(self):
        """ Tests whether the correct homepage template is used """
        r = self.client.get(reverse('home'))
        self.assertEquals(r.status_code, 200)
        self.assertTemplateUsed(r, 'hardware_models/homepage.html')

    # def test_homepage_is_paginated(self):
    #     """ Tests whether the homepage is paginated (as it should be) """
    #     r = self.client.get(reverse('homepage'))
    #     self.assertEquals('is_paginated' in r.context)
    #     self.assertTrue(r.context['is_paginated'] is True)
    #     self.assertTrue(len(r.context['post_list']) == 3)  # assumes we are going to have 3 posts as an example

    def test_list_all_posts(self):
        """ Tests whether all posts is listed correctly """
        r = self.client.get(reverse('home'))
        self.assertEquals(r.status_code, 200)

    # def test_list_all_posts(self):
    #     """ Tests whether all posts is listed correctly """
    #     r = self.client.get(reverse('home'))
    #     self.assertEquals(r.status_code, 200)

    def tearDown(self):
        pass
