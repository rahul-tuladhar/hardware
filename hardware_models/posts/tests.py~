from django.test import TestCase
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from posts.models import Post
from login.models import Profile, Group




# Create your tests here.
class PostViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    # test cases for the experience layer api

    def tearDownTestData(cls):
        pass



class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""

        Group.objects.create(location="Charlottesville", name="CAV computing")
        Profile.objects.create(
            # affiliations = "CAV computing",
            display_name="FirstUser",
            email='firstuser@gmail.com',
            password='password',
            username='FirstUsername'
        )
        Post.objects.create(
            title="AMD RYZEN 7 1700X 8-Core 3.4 GHz",
            description="New: A brand-new, unused",
            part="CPU",
            author=Profile.objects.get(display_name="FirstUser"),
            payment_method="Paypal",
            price="264.99 ",
            transaction_type="Selling"
        )
        Post.objects.create(
            title="Kingston HyperX Fury 8GB DDR4 SDRAM Memory Module",
            description="Used: Still in good condition, 1 year of use",
            part="SDRAM",
            author=Profile.objects.get(display_name="FirstUser"),
            payment_method="Cash",
            price="72.99",
            transaction_type="Buying"
        )
        Post.objects.create(
            title="""Acer XR341CK bmijpphz Black 34""",
            description="Brand new: Product in original packaging",
            part="Monitor",
            author=Profile.objects.get(display_name="FirstUser"),
            payment_method="Cash",
            price="549.99",
            transaction_type="Trading",
            location='Charlottesville'
        )

    # TODO: FIX get(author =1 ) returns multiple objects
    # def test_author_label(self):
    #     post = Post.objects.get(author = 1)
    #     field_label = post._meta_.get_field('author').verbose_name
    #     self.assertEquals(field_label, 'author')

    # TODO: FIX how to get() an actual datetime 
    # def test_date_label(self):
    #     post = Post.objects.get(date = '')
    #     field_label = post._meta.get_field('date').verbose_name
    #     self.assertEquals(field_label, 'date')

    def test_description_label(self):
        """ Tests the post's label. """

        post = Post.objects.get(description='New: A brand-new, unused')
        field_label = post._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_location_label(self):
        """ Tests the post's label. """

        post = Post.objects.get(location='Charlottesville')
        field_label = post._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_part_label(self):
        """ Tests the post's label. """

        post = Post.objects.get(part='CPU')
        field_label = post._meta.get_field('part').verbose_name
        self.assertEquals(field_label, 'part')

    def test_payment_method_label(self):
        """ Tests the post's label. """

        post = Post.objects.get(payment_method='Paypal')
        field_label = post._meta.get_field('payment_method').verbose_name
        self.assertEquals(field_label, 'payment method')

    def test_title_max_length(self):
        """ Tests the post's label. """

        post = Post.objects.get(title='AMD RYZEN 7 1700X 8-Core 3.4 GHz')
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)

    def test_post_name_is_title(self):
        """ Tests the string method. """

        post = Post.objects.get(title='AMD RYZEN 7 1700X 8-Core 3.4 GHz')
        expected_post_name = '%s' % (post.title)
        self.assertEquals(expected_post_name, str(post))

    # TODO: Create a get_absolute_url(self): method in Post.models
    # def test_get_absolute_url(self):
    #     author=Author.objects.get(id=1)
    #     #This will also fail if the urlconf is not defined.
    #     self.assertEquals(author.get_absolute_url(),'/catalog/author/1')


