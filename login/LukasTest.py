from django.test import TestCase
from login.forms import PlaylistForm, SongForm, AddPreferencesForm, UserForm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from login.views import delete_song, delete_playlist, create_song, create_playlist
from django.shortcuts import render, get_object_or_404

class InvalidRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_invalid_register(self):
        driver = self.driver
        driver.get(self.base_url + "register/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("luke")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("luke")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
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

class ValidRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_valid_register(self):
        driver = self.driver
        driver.get(self.base_url + "register/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("5")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("luke@yahoo.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class ValidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Valid_login(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("1")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class InvalidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Valid_login(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("1")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("lulu")
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

class ValidLoginAndAddPL(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_valid_login_AndAddPL(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("1")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys("Test Playlist")
        driver.find_element_by_css_selector("button.btn.btn-success").click()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class ValidLoginAddPLAndPref(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_Add_PL_And_Pref(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("2")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys("Test Playlist")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Rock")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Hip Hop")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Gangster Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Conscious Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class ValidRegisterAndAddSongs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_valid_register_And_Add_Songs(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("3")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys("Test Playlist")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Rock")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Hip Hop")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Gangster Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Conscious Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("What Is Love")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Love")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Baby Dont Hurt Me")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Dont Hurt Me")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("No More")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("ooOHOH")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("WOAHWOAH")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("ooWOAHWOAH")
        driver.find_element_by_css_selector("button.btn.btn-success").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class ViewDetail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_view_detail(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("3")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("View Details").click()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class DeletePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_delete_playlist(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("3")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_css_selector("button.btn.btn-sm").click()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class ValidLoginAddPLAndPrefToExisting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_Add_PL_And_Pref(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("1")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("View Details").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Rock")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Hip Hop")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Gangster Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("Conscious Rap")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class ValidLoginAddPLAndSongsToExisting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_Add_PL_And_Pref(self):
        driver = self.driver
        driver.get(self.base_url + "login/login_user/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("1")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("luke")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("View Details").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("What Is Love")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Love")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Baby Dont Hurt Me")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Dont Hurt Me")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("No More")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("ooOHOH")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("WOAHWOAH")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("ooWOAHWOAH")
        driver.find_element_by_css_selector("button.btn.btn-success").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
