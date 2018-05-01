from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import unittest

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
	    self.driver = webdriver.Remote(
	    command_executor='http://selenium-chrome:4444/wd/hub',
	    desired_capabilities=DesiredCapabilities.CHROME)

	def test_login(self):
		driver = self.driver
        driver.get('http://localhost:8000/login/')

        # find form fields
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_id("submit")

        # clear them
        username.clear()
        password.clear()
        submit.clear()

        # send stuff
        username.send_keys("kyan")
		username.send_keys(Keys.RETURN)

		# returned stuff
		assert "No results found." not in driver.page_source

	# def test_logout(self):
	# 	driver = self.driver
 #        driver.get('http://localhost:8000/logout/')

	def test_register(self):
		driver = self.driver
        driver.get('http://localhost:8000/register/')

	def test_add_post(self):
		driver = self.driver
        driver.get('http://localhost:8000/add_post/')

	# def testSearchPost(self):
	# 	driver = self.driver
 #        driver.get('http://web:8000/login/')

 	def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()