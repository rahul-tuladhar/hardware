# from django.test import TestCase, Client
# from django.core.urlresolvers import reverse
# from posts.models import Post, Review
# Create your tests here.

# Tests should now be in the /tests directory

# class GetReviewPageTestCase(TestCase):
# 	# setUp() is called before each test in this class
# 	def setUp(self):
# 		pass

# 	def success_response(self):
# 		# .client initiates a dummy browser
# 		response = self.client.get()

# 		#Checks that the HTTP response code is 200
# 		self.assertContains(response, '')

# 	def fails_invalid(self):
# 		response = self.client.get()
# 		self.assertEquals(response.status_code, 404)

# 	# tearDown() is called at the end of each test
# 	def tearDown(self):
# 		pass