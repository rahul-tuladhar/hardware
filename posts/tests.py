from django.test import TestCase
from posts.models import Post

# Create your tests here.
class GetPostDetailPageTestCase(TestCase):
	#setUp() is called before each test
	def setUp(self):
		Post.objects.create(
			title = "AMD RYZEN 7 1700X 8-Core 3.4 GHz",
			description = "New: A brand-new, unused",
			author = "AMD",
			part = "CPU",
			payment_method = "Paypal",
			price = "$264.99 ",
			transaction_type = "Selling"
		)
		Post.objects.create(
			title = "Kingston HyperX Fury 8GB DDR4 SDRAM Memory Module",
			description = "Used: Still in good condition, 1 year of use",
			author = "Kingston",
			part = "SDRAM",
			payment_method = "Cash",
			price = "$72.99",
			transaction_type = "Buying"
		)
		Post.objects.create(
			title = """Acer XR341CK bmijpphz Black 34, 21:9 WQHD Curved 
			, 3440 x 1440 LED IPS Monitor, Adaptive-Sync( Free-Sync) 
			with DTS® Sound Speakers, USB 3.0, HDMI, MHL, Display Port""",
			description = "Brand new: Product in original packaging",
			author = "Acer",
			part = "Monitor",
			payment_method = "Cash",
			price = "$549.99",
			transaction_type = "Trading"
		)
		# Every test needs a client
		self.client = Client() 

	def successful_all_posts_response(self):
		response = self.client.get(reverse('index',kwargs = {}))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '1')

	def invalid_all_posts_response(self):
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 404)

	def valid_posts(self):
		cpu = Post.objects.get(part = "CPU")
		sdram = Post.objects.get(part = "SDRAM")
		monitor = Post.objects.get(part = "Monitor")
		response = self.client(get('/'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context['posts']), 3)

	def valid_post_details(self):
		cpu = Post.objects.get(part= "CPU")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context[''])

	def tearDown(self):
		pass 