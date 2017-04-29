from selenium import webdriver
import unittest
from .Data import LoginDataGenerate
import MySQLdb


class GenerateSongsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_generate_songs(self):
        driver = self.driver
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Generate Recommendations')])[2]").click()
        res = driver.find_element_by_css_selector("ul > a")
        link = res.get_attribute("href")
        driver.find_element_by_link_text('Logout').click()
if __name__ == "__main__":
    unittest.main()


class GenerateSongsTestDiff(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_generate_songs_diff(self):
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur = conn1.cursor()
        driver = self.driver
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Generate Recommendations')])[2]").click()
        res = driver.find_element_by_css_selector("ul > a")
        link = res.get_attribute("href")
        arr = link.split('/')
        driver.find_element_by_link_text("profiles").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Generate Recommendations')])[1]").click()
        res1 = driver.find_element_by_css_selector("ul > a")
        link1 = res1.get_attribute("href")
        arr1 = link1.split('/')
        print(arr[len(arr)-2])
        print(arr1[len(arr1) - 2])
        self.assertNotEqual(arr[len(arr)-2],arr1[len(arr1) - 2])
        driver.find_element_by_link_text('Logout').click()
        cur.execute(
            "delete from login_song where login_song.playlist_id in ( select id from login_playlist where Plalyst_title = 'test_pl')")
        cur.execute("commit")
        cur.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cur.execute("delete from login_playlist where Plalyst_title = 'test_pl'")
        cur.execute("SET FOREIGN_KEY_CHECKS = 1;")
        cur.execute("commit")
        cur.close()
        conn1.close()
if __name__ == "__main__":
    unittest.main()

class GenerateSongsTestSame(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_generate_songs_same(self):
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur = conn1.cursor()
        driver = self.driver
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Generate Recommendations')])[2]").click()
        res = driver.find_element_by_css_selector("ul > a")
        link = res.get_attribute("href")
        arr = link.split('/')
        driver.find_element_by_link_text("profiles").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Generate Recommendations')])[1]").click()
        res1 = driver.find_element_by_css_selector("ul > a")
        link1 = res1.get_attribute("href")
        arr1 = link1.split('/')
        print(arr[len(arr)-2])
        print(arr1[len(arr1) - 2])
        self.assertEqual(arr[len(arr)-2],arr1[len(arr1) - 2])
        driver.find_element_by_link_text('Logout').click()
        cur.execute(
            "delete from login_song where login_song.playlist_id in ( select id from login_playlist where Plalyst_title = 'test_pl')")
        cur.execute("commit")
        cur.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cur.execute("delete from login_playlist where Plalyst_title = 'test_pl'")
        cur.execute("SET FOREIGN_KEY_CHECKS = 1;")
        cur.execute("commit")
        cur.close()
        conn1.close()
if __name__ == "__main__":
    unittest.main()

