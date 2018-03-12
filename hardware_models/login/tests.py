from django.test import TestCase
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from posts.models import Post
from login.models import Profile, Group


#Views tests
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


#Models tests
class LoginModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        :return: None
        """
        Group.objects.create(location="Charlottesville", name="CAV computing")
        Profile.objects.create(
            # affiliations = "CAV computing",
            display_name="FirstUser",
            email='firstuser@gmail.com',
            password='password',
            username='FirstUsername'
        )

    # Each test tests a specific 'label' or model attribute
    # GROUP
    def test_group_location_label(self):
        """ Tests the group's label. """

        group = Group.objects.get(location='Charlottesville')
        field_label = group._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_group_location_max_length(self):
        """ Tests the max length of the attribute. """

        group = Group.objects.get(location='Charlottesville')
        max_length = group._meta.get_field('location').max_length
        self.assertEquals(max_length, 50)

    def test_group_name_label(self):
        """ Tests the group's label. """

        group = Group.objects.get(name='CAV computing')
        field_label = group._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_group_name_max_length(self):
        """ Tests the max length of the attribute. """

        group = Group.objects.get(name='CAV computing')
        max_length = group._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_group_name_is_name(self):
        """ Tests the to string method. """

        group = Group.objects.get(name='CAV computing')
        expected_group_name = '%s' % (group.name)
        self.assertEquals(expected_group_name, str(group))

    # PROFILE
    # def test_profile_affilliations_label(self):
    #     profile= Profile.objects.get(affiliations ='CPU')
    #     field_label = profile._meta.get_field('part').verbose_name
    #     self.assertEquals(field_label,'part')

    def test_profile_display_name_label(self):
        """ Tests the profile's label. """

        profile = Profile.objects.get(display_name='FirstUser')
        field_label = profile._meta.get_field('display_name').verbose_name
        self.assertEquals(field_label, 'display name')

    def test_profile_display_name_max_length(self):
        """ Tests the max length of the attribute. """

        profile = Profile.objects.get(display_name='FirstUser')
        max_length = profile._meta.get_field('display_name').max_length
        self.assertEquals(max_length, 24)

    def test_profile_email_label(self):
        """ Tests the profile's label. """

        profile = Profile.objects.get(email='firstuser@gmail.com')
        field_label = profile._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_profile_email_max_length(self):
        """ Tests the max length of the attribute. """

        profile = Profile.objects.get(email='firstuser@gmail.com')
        max_length = profile._meta.get_field('email').max_length
        self.assertEquals(max_length, 254)

    def test_profile_username_label(self):
        """ Tests the profile's label. """

        profile = Profile.objects.get(username='FirstUsername')
        expected_profile_name = '%s' % (profile.username)
        self.assertEquals(expected_profile_name, str(profile))

    def test_profile_username_max_length(self):
        """ Tests the max length of the attribute. """

        profile = Profile.objects.get(username='FirstUsername')
        max_length = profile._meta.get_field('username').max_length
        self.assertEquals(max_length, 24)


