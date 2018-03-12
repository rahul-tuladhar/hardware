from django.test import TestCase, Client
from django.core.urlresolvers import reverse

# Create your tests here.
# class GetUserProfileTestCase(TestCase):
# 	def setUp(self):
# 		#Every test needs a client to similuate a browser
# 		self.client = Client()

# 	# def test_successful_userprofile_response(self):
# 	# 	response = self.client.get(reverse('user_profile', args=['api/v1/users/rahultuladhar']))
# 	# 	self.assertEqual(response.status_code, 200)
# 	def teardown(self):
# 		pass