from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LoginTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(LoginTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/register/')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        email_address= selenium.find_element_by_id('id_email_address')
        password = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        username.send_keys('gouthami')
        email_address.send_keys('gouth@gmail.com')
        password.send_keys('gouthu')


        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Check your email' in selenium.page_source

    def ui_test_one(self):
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/create_playlist/')
        addplaylist= selenium.find_element_by_id('add_playlist')
        # Fill the form with data
        addplaylist.send_keys('Rock')
        # submitting the form
        submit.send_keys(Keys.RETURN)

        # check the returned result
        assert 'Check the name of playlist' in selenium.page_source
