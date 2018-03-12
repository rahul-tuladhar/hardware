# from django.test import TestCase, Client
# from django.core.urlresolvers import reverse
# from posts.models import Post
# from login.models import Profile, Group

# Tests should be set up in the /tests directory
# Create your tests here.
# class GetPostDetailPageTestCase(TestCase):
# 	#setUp() is called before each test
# 	def setUp(self):
		
# 		# Every test needs a client
# 		self.client = Client() 
# 	# test functions must have 'test' at the start of the function
# 	def test_successful_all_posts_response(self):
# 		response = self.client.get(reverse('index',kwargs = {}))
# 		self.assertEqual(response.status_code, 200)
# 		# self.assertContains(response, '1')

# 	# def test_invalid_all_posts_response(self):
# 	# 	response = self.client.get(reverse('index'))
# 	# 	self.assertEqual(response.status_code, 404)

# 	# def test_valid_posts(self):
# 	# 	cpu = Post.objects.get(part = "CPU")
# 	# 	sdram = Post.objects.get(part = "SDRAM")
# 	# 	# monitor = Post.objects.get(part = "Monitor")
# 	# 	response = self.client.get(reverse('post_detail'))
# 	# 	self.assertEqual(response.status_code, 200)
# 	# 	# self.assertEqual(len(response.context['posts']), 3)

# 	# def test_valid_post_details(self):
# 	# 	cpu = Post.objects.get(part= "CPU")
# 	# 	response = self.client.get(reverse('post_detail'))
# 	# 	self.assertEqual(response.status_code, 200)
# 	# 	# self.assertEqual(response.context[''])

# 	def tearDown(self):
# 		pass 