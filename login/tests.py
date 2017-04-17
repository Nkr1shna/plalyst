from django.test import TestCase
from login.forms import PlaylistForm,SongForm,AddPreferencesForm,UserForm
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


class CreatePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_playlist(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gouthu123")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("gouthu123")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add Plalyst").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys("playlist2")
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


class AddPreferences(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_preferences(self):
        driver = self.driver
        driver.get(self.base_url + "login/")
        driver.find_element_by_link_text("View Details").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("rock")
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


class CreateSong(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_song(self):
        driver = self.driver
        driver.get(self.base_url + "login/19/create_song/")
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("heart wants what it wants")
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


class DeleteAlbum(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_delete_album(self):
        driver = self.driver
        driver.get(self.base_url + "login/")
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


class Logout2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_logout2(self):
        driver = self.driver
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("gouthu123")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("gouthu123")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Logout").click()

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
    def test_delete_playlist():
        assert delete_playlist('POST',111) == render('POST', 'detail.html', {'playlist': Playlist.objects.get(pk=111)})  
        

class FormTests(TestCase):
    def test_forms(self):
        form_data = {'Plalyst_title': 'Rockmusiclist'}
        form = PlaylistForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form1(self):
        form_data = {'song_title': 'Shape of you'}
        form = SongForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form2(self):
        form_data = {'preferences': 'Jazz'}
        form = AddPreferencesForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form3(self):
        form_data= {'username':'gouthu',
                    'email':'gouthu123@gmail.com',
                    'password':'gouthu'}
        form= UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form4(self):
        form_data = {'username': 'gouthu',
                     'email': 'gouthu123',
                     'password': 'gouthu'}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())

def test_delete_song():
    assert delete_song('POST',111,222)== render('POST','detail.html', {'playlist': get_object_or_404(Playlist, pk=111)})

def test_delete_playlist():
    assert delete_playlist('POST',111) == render('POST', 'detail.html', {'playlist': Playlist.objects.get(pk=111)})
    
def test_create_song_pass():
    assert create_song('POST',111)==('POST', 'detail.html', {'playlist': get_object_or_404(Playlist, pk=111)})
    
def test_logout_user():
    assert logout_user(x) == render(x, 'login.html', context)

def test_add_preference():
    assert add_preferences(x,111) == render(x, 'add_preferences.html', context)
