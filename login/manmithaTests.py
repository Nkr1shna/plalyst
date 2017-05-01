from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from django.test import TestCase
from django.test.client import Client
from .Data import RegisterDetails, LoginData, PlaylistName, inputSong
from login.forms import AddPreferencesForm,UserForm, LoginForm

class CreatePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_playlist(self):
        user=LoginData()
        driver = self.driver
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add Plalyst").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys(PlaylistName())
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



class DeletePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_delete_playlist(self):
        driver = self.driver
        user = LoginData()
        driver.get(self.base_url + "/login/logout_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys(PlaylistName())
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("profiles").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
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

class Logout2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_logout2(self):
        driver = self.driver
        user = LoginData()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
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


class FormTests(TestCase):
    def PlaylistForm(self):
        form_data = {'preferences': PlaylistName()}
        form = AddPreferencesForm(data=form_data)
        self.assertTrue(form.is_valid())

    def LoginDataForm(self):
        user=LoginData()
        form_data= {'username':user.name,
                    'password':user.password}
        form= LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def RegisterForm(self):
        user=RegisterDetails()
        form_data= {'username':user.name,
                    'email':user.email,
                    'password':user.password}
        form= UserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def InvalidRegisterForm(self):
        user = RegisterDetails()
        form_data = {'username':user.name,
                     'email':user.invalidEmail ,
                     'password': user.password}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())

class URLTest(unittest.TestCase):
    def Create_Play(self):
        client = Client()
        response = client.get('http://localhost:8000/login/create_playlist/')
        self.assertEqual(response.status_code, 200)


class Register(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_register(self):
        driver = self.driver
        user=RegisterDetails()
        driver.get(self.base_url + "login/register/")
        driver.find_element_by_link_text("Register").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys(user.email)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
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

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        user = LoginData()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
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
        songList = inputSong()
        driver = self.driver
        user = LoginData()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add Plalyst").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys(PlaylistName())
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songList[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("View All").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
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