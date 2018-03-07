from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from login.views import user_profile
from posts.views import index, post_detail, edit_post


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


	def tearDownTestData(cls):
		pass

class ReviewViewTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		pass


	def tearDownTestData(cls):
		pass