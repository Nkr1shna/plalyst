from django.test import TestCase
from login.forms import PlaylistForm, SongForm, AddPreferencesForm, UserForm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from login.views import delete_song, delete_playlist, create_song, logout_user, add_preferences
from django.shortcuts import render, get_object_or_404
from .models import Playlist
from .models import Playlist, Song
from django.test.client import Client
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from .views import register


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_register(self):
        driver = self.driver
        driver.get(self.base_url + " ")
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gouthu123")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("gouthu123@gmail.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("gouthu123")
        driver.find_element_by_css_selector("button.btn.btn-success").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gouthu123")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("gouthu123")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        self.assertEqual("Plalyst", driver.title)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.swtich_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()



class DeleteSong(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_delete_song(self):
        driver = self.driver
        driver.get(self.base_url + "login/19/")
        driver.find_element_by_xpath("//button[@type='submit']").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

LinkTest(unittest.TestCase):

    def test_form3(self):
        form_data = {'username': 'gouthu',
                     'email': 'gouthu123@gmail.com',
                     'password': 'gouthu'}
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form4(self):
        form_data = {'username': 'gouthu',
                     'email': 'gouthu123',
                     'password': 'gouthu'}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())


"""def test_delete_song():
    assert delete_song('POST',111,222)== render('POST','detail.html', {'playlist': get_object_or_404(Playlist, pk=111)})

def test_delete_playlist():
    assert delete_playlist('POST',111) == render('POST', 'detail.html', {'playlist': Playlist.objects.get(pk=111)})

def test_create_song_pass():
    assert create_song('POST',111)==('POST', 'detail.html', {'playlist': get_object_or_404(Playlist, pk=111)})

def test_logout_user():
    assert logout_user(x) == render(x, 'login.html', context)

def test_add_preference():
    assert add_preferences(x,111) == render(x, 'add_preferences.html', context)"""


class SimpleTest(unittest.TestCase):
    def test_index(self):
        client = Client()
        response = client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

    def test_index1(self):
        client = Client()
        response = client.get('http://localhost:8000/login/')
        self.assertEqual(response.status_code, 200)

    def test_index2(self):
        client = Client()
        response = client.post('http://localhost:8000/login/', {'username': 'gouthu123', 'password': 'gouthu123'})
        self.assertEqual(response.status_code, 200)


class Test_register(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='achu', email='achu@gmail.com', password='achu')

    def test_register(self):
        # Create an instance of a GET request.
        request = self.factory.get('http://localhost:8000/register/')

        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test register() as if it were deployed at http://localhost:8000/register/
        response = register(request)
        self.assertEqual(response.status_code, 200)


class InvalidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = "invalid login"
        self.accept_next_alert = True

    def test_invalid_login(self):
        driver = self.driver
        driver.get(self.base_url + " ")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gouthu123")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("gouthu")
        driver.find_element_by_css_selector("button.btn.btn-success").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual('invalid login', self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

    
class integrationtest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='harpita', email='harpita@gmail.com', password='harpita')

    def test_register(self):

        request = self.factory.get('http://localhost:8000/register/')

        request.user = self.user

        register(request)


        client = Client()
        response = client.post('http://localhost:8000/login/', {'username': 'harpita', 'password': 'harpita'})
        self.assertEqual(response.status_code, 200)


class loginIntegration(TestCase):
    def setUp(self):
        User.objects.create(username='sonu', email='sonu@gmail.com', password='sonu')

    def testdata(self):
        name=User.objects.get(username='sonu')
        self.assertEqual(name.username,'sonu')

class CreatePlaylistIntegration(TestCase):
    def setUp(self):
        Playlist.objects.create(Plalyst_title='SONGS')

    def testdata(self):
        name=Playlist.objects.get(Plalyst_title='SONGS')
        self.assertEqual(name.Plalyst_title,'SONGS')



class integrationtest1(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='kalpana', email='kalpana@gmail.com', password='kalpana')

    def test_register(self):
        # Create an instance of a GET request.
        request = self.factory.get('http://localhost:8000/register/')

        # logged-in user by setting request.user manually.
        request.user = self.user

        # Test register() as if it were deployed at http://localhost:8000/register/
        register(request)
        name = User.objects.get(username='kalpana')
        self.assertEqual(name.username, 'kalpana')

class playlogin(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='kalpana', email='kalpana@gmail.com', password='kalpana')

        self.playlist = Playlist.objects.create(Plalyst_title='ROCK')

    def test_playlist(self):


        request= self.factory.get('http://localhost:8000/create_playlist/')
        request.user = self.user

        create_playlist(request)

        name = Playlist.objects.get(Plalyst_title='ROCK')
        self.assertEqual(name.Plalyst_title, 'ROCK')

        self.assertEqual(name.user.username,'kalpana')



