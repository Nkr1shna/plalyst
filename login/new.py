import unittest, time
from selenium import webdriver
from .Data import LoginDataGenerate, PlaylistName

class AddPreferences(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_preferences(self):
        print("Add Pref")
        driver = self.driver
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("View Details").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("rock")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("pop")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys("punk")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Devoid of Light")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("What a Difference a Day Makes")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Big And Sad")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Paper")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Whistle")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Ormadans")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("I Don't Know (Gotta Have You)")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys("Pusta studnia")
        driver.find_element_by_css_selector("button.btn.btn-success").click()


if __name__ == "__main__":
    unittest.main()
