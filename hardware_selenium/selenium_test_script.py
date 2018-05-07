from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import unittest
import re

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
	    self.driver = webdriver.Remote(
	    command_executor='http://selenium-chrome:4444/wd/hub',
	    desired_capabilities=DesiredCapabilities.CHROME)

    def test_register(self):
        driver = self.driver
        driver.get('web:8000/register/')

        # find form fields
        username = driver.find_element_by_id("id_username")
        name = driver.find_element_by_id("id_display_name")
        email = driver.find_element_by_id("id_email")
        password = driver.find_element_by_id("id_password")
        register = driver.find_element_by_id("id_register")

        # clear them
        username.clear()
        name.clear()
        email.clear()
        password.clear()

        #send stuff
        username.send_keys("none")
        name.send_keys("Kat Yan")
        email.send_keys("test2@gmail.com")
        password.send_keys("none")
        register.submit();

        #see if the user got registerd
        source = driver.page_source
        found = re.search(r'register', source)
        value = self.assertNotEqual(found, None)

        # # login with registered user
        # login_username = driver.find_element_by_id("id_username")
        # login_password = driver.find_element_by_id("id_password")
        # submit = driver.find_element_by_id("id_login")
        # login_username.clear()
        # login_password.clear()
        # login_username.send_keys("none2")
        # login_password.send_keys("none2")
        # submit.submit()

    def test_login(self):
    	driver = self.driver
    	driver.get("web:8000/login/")

    	# find form fields
    	username = driver.find_element_by_id("id_username")
    	password = driver.find_element_by_id("id_password")
    	submit = driver.find_element_by_id("id_login")

    	# clear them
    	username.clear()
    	password.clear()

    	# send stuff
    	username.send_keys("none")
    	password.send_keys("none")
    	submit.submit()

    	#see if the user got logged in
    	source = driver.page_source
    	found = re.search(r'Welcome to the homepage', source)
    	value = self.assertNotEqual(found, None)

    def test_logout(self):
    	driver = self.driver
    	driver.get('web:8000/login/')

    	# find form fields
    	login_username = driver.find_element_by_id("id_username")
    	login_password = driver.find_element_by_id("id_password")
    	submit = driver.find_element_by_id("id_login")

    	# clear them
    	login_username.clear()
    	login_password.clear()

    	# send stuff
    	login_username.send_keys("none")
    	login_password.send_keys("none")
    	submit.submit()

    	#find fields from home page
    	logout = driver.find_element_by_id("id_logout")
    	logout.submit()

    	#see if user was logged out
    	source = driver.page_source
    	found = re.search(r'You have successfully logged out', source)
    	value = self.assertNotEqual(found, None)

    def test_add_post(self):
    	driver = self.driver
    	driver.get("web:8000/login/")

    	#login with registered user
    	username = driver.find_element_by_id("id_username")
    	password = driver.find_element_by_id("id_password")
    	submit = driver.find_element_by_id("id_login")
    	username.clear()
    	password.clear()
    	username.send_keys("none")
    	password.send_keys("none")
    	submit.submit()

    	#find the add post page
    	add_post = driver.find_element_by_id("add_post")
    	add_post.submit()

    	#find fields of post
    	title = driver.find_element_by_id("id_title")
    	price = driver.find_element_by_id("id_price")
    	part = driver.find_element_by_id("id_part")
    	description = driver.find_element_by_id("id_description")
    	location = driver.find_element_by_id("id_location")
    	payment = driver.find_element_by_id("id_payment_method")
    	transaction = driver.find_element_by_id("id_transaction_type")
    	submit_post = driver.find_element_by_id("add_post_button")

    	#create post
    	title.send_keys("Selenium test")
    	price.send_keys("20.00")
    	part.send_keys("Backend")
    	description.send_keys("A test")
    	location.send_keys("Charlottesville")
    	payment.send_keys("Cash")
    	transaction.send_keys("Buying")
    	submit_post.submit()

    	#see if it worked
    	source = driver.page_source
    	found = re.search(r'Selenium test', source)
    	value = self.assertNotEqual(found, None)

    def test_search_post(self):
    	driver = self.driver
    	driver.get('web:8000/login/')

        #search something
        search_field = driver.find_element_by_id("id_search_field")
        search = driver.find_element_by_id("id_search")
        serach_field.send_keys("a")
        search.submit()

        #see if it worked
        source = driver.page_source
        found = re.search(r'No results', source)
        value = self.assertNotEqual(found, None)

    def tearDown(self):
    	self.driver.close()

if __name__ == "__main__":
	unittest.main()