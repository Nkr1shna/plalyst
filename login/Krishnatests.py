from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from login.forms import PlaylistForm, SongForm
from django.test import TestCase
from django.test.client import Client
from .Data import LoginData, PlaylistName, inputSong, LoginDataGenerate
import time


class GeneratePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_generate_playlist(self):
        driver = self.driver
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Generate Recommendations").click()
        driver.find_element_by_link_text('Logout').click()


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
        user=LoginData()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.username)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("View Details").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(PlaylistName())
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
        songList=inputSong()
        driver = self.driver
        driver.get(self.base_url + "login/19/create_song/")
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songList[0])
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


class Youtube(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_youtube(self):
        driver = self.driver
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Generate Recommendations").click()
        driver.find_element_by_link_text("(ii) Falter").click()
        time.sleep(10)
        driver.find_element_by_link_text('Logout').click()



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

class FormTests(TestCase):
    def test_forms(self):
        form_data = {'Plalyst_title': 'Rockmusiclist'}
        form = PlaylistForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form1(self):
        form_data = {'song_title': 'Shape of you'}
        form = SongForm(data=form_data)
        self.assertTrue(form.is_valid())

class URL(unittest.TestCase):
    def GenerateTest(self):
        client = Client()
        response = client.get('http://localhost:8000/generate/')
        self.assertEqual(response.status_code, 200)




