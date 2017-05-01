import csv
from socket import socket

from TestLibrary.Parser import file, filepref, filereg
from selenium import webdriver
import unittest
from .Data import LoginDataGenerate
import MySQLdb
import time
from statistics import mean,median,stdev
import matplotlib.pyplot as plt
from .Data import PlaylistName, RegisterDetails
#from TestLibrary.DataLibrary import RegisterDetails
class GenerateSongsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_generate_songs_test(self):
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


class FullFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_fullfunctionality(self):
        user=RegisterDetails()
        driver = self.driver
        with open('TestLibrary/' + file) as csvfile:
            songs = csv.reader(csvfile, delimiter='"', quotechar='|')
            songslist=[]
            for row in songs:
                songslist.append(row)
        with open('TestLibrary/' + filepref) as csvfile:
            preferences = csv.reader(csvfile, delimiter='"', quotechar='|')
            preferencelist=[]
            for row in preferences:
                preferencelist.append(row)
        driver.get(self.base_url + "login/register/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys(user.email)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add Plalyst").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys("basaFishPlaylist")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[1])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[2])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[1])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[2])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[3])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[4])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[5])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[6])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[7])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Generate Recommendations").click()
        driver.find_element_by_link_text("Evil Little Goat").click()
        driver.find_element_by_link_text("Der zweite Teil der Ewigkeit").click()
        driver.find_element_by_link_text("Logout").click()
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur = conn1.cursor()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0; delete from login_song where playlist_id in " +
                    "(select id from login_playlist where Plalyst_title = 'basaFishPlaylist');" +
                    "delete from login_playlist where Plalyst_title = 'basaFishPlaylist'; " +
                    "delete from auth_user where username = 'basafish'; " +
                    "SET FOREIGN_KEY_CHECKS = 1;  commit;")
        cur.close()
        conn1.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = driver.switch_to_alert()
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


class FullFunctionalityTimeGraph(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_function_calls(self):
        ar = []
        for i in range(0, 10):
            t = time.time()
            self.assertTrue(None == self.fullfunctionality_time())
            ar.append(time.time() - t - 7)
        plt.plot(ar)
        plt.ylabel('Time taken in s')
        plt.show()
    def fullfunctionality_time(self):
        t = time.time()
        driver = self.driver
        with open('TestLibrary/' + file) as csvfile:
            songs = csv.reader(csvfile, delimiter='"', quotechar='|')
            songslist=[]
            for row in songs:
                songslist.append(row)
        with open('TestLibrary/' + filepref) as csvfile:
            preferences = csv.reader(csvfile, delimiter='"', quotechar='|')
            preferencelist=[]
            for row in preferences:
                preferencelist.append(row)
        driver.get(self.base_url + "login/register/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("basafish")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("basa@fish.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("basafish")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("basafish")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("basafish")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add Plalyst").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys("basaFishPlaylist")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[1])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[2])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[1])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[2])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[3])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[4])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[5])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[6])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[7])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Generate Recommendations").click()
        driver.find_element_by_link_text("Evil Little Goat").click()
        driver.find_element_by_link_text("Der zweite Teil der Ewigkeit").click()
        driver.find_element_by_link_text("Logout").click()
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur = conn1.cursor()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0; delete from login_song where playlist_id in " +
                    "(select id from login_playlist where Plalyst_title = 'basaFishPlaylist');" +
                    "delete from login_playlist where Plalyst_title = 'basaFishPlaylist'; " +
                    "delete from auth_user where username = 'basafish'; " +
                    "SET FOREIGN_KEY_CHECKS = 1;  commit;")
        cur.close()
        conn1.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = driver.switch_to_alert()
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

class FullFunctionalityTime(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_function_calls(self):
        ar = []
        for i in range(0, 10):
            t = time.time()
            self.assertTrue(None == self.fullfunctionality_time())
            ar.append(time.time() - t - 7)
        print("The timings are:")
        print(ar)
        print("Mean:")
        print(mean(ar))
        print("Median:")
        print(median(ar))
        print("STD deviation:")
        print(stdev(ar))

    def fullfunctionality_time(self):
        t = time.time()
        with open('TestLibrary/' + file) as csvfile:
            songs = csv.reader(csvfile, delimiter='"', quotechar='|')
            songslist=[]
            for row in songs:
                songslist.append(row)
        with open('TestLibrary/' + filepref) as csvfile:
            preferences = csv.reader(csvfile, delimiter='"', quotechar='|')
            preferencelist=[]
            for row in preferences:
                preferencelist.append(row)
        name=RegisterDetails().name
        email=RegisterDetails().email
        password=RegisterDetails().password
        driver = self.driver
        driver.get(self.base_url + "login/register/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(name)
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys(email)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add Plalyst").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys(PlaylistName())
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[1])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Preferences").click()
        driver.find_element_by_id("id_preferences").clear()
        driver.find_element_by_id("id_preferences").send_keys(preferencelist[2])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[1])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[2])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[3])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[4])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[5])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[6])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[7])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Generate Recommendations").click()
        driver.find_element_by_link_text("Evil Little Goat").click()
        driver.find_element_by_link_text("Der zweite Teil der Ewigkeit").click()
        driver.find_element_by_link_text("Logout").click()
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur = conn1.cursor()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0; delete from login_song where playlist_id in " +
                    "(select id from login_playlist where Plalyst_title = 'basaFishPlaylist');" +
                    "delete from login_playlist where Plalyst_title = 'basaFishPlaylist'; " +
                    "delete from auth_user where username = 'basafish'; " +
                    "SET FOREIGN_KEY_CHECKS = 1;  commit;")
        cur.close()
        conn1.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = driver.switch_to_alert()
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


class Rec30(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_rec_30(self):
        driver = self.driver
        with open('TestLibrary/' + file) as csvfile:
            songs = csv.reader(csvfile, delimiter='"', quotechar='|')
            songslist=[]
            for row in songs:
                songslist.append(row)
        driver.get(self.base_url + "login/register/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("basafish")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("basa@fish.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("basafish")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add Plalyst").click()
        driver.find_element_by_id("id_Plalyst_title").clear()
        driver.find_element_by_id("id_Plalyst_title").send_keys("basaFishPlaylist")
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Add New Song").click()
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[0])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[1])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[2])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[3])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[4])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[5])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[6])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        time.sleep(1)
        driver.find_element_by_id("id_song_title").clear()
        driver.find_element_by_id("id_song_title").send_keys(songslist[7])
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Generate Recommendations").click()
        time.sleep(10)
        list_of_links = driver.find_elements_by_tag_name("a")
        self.assertTrue(len(list_of_links)-4, 30)
        driver.find_element_by_link_text("Logout").click()
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur = conn1.cursor()
        cur.execute("SET FOREIGN_KEY_CHECKS = 0; delete from login_song where playlist_id in " +
                    "(select id from login_playlist where Plalyst_title = 'basaFishPlaylist');" +
                    "delete from login_playlist where Plalyst_title = 'basaFishPlaylist'; " +
                    "delete from auth_user where username = 'basafish'; " +
                    "SET FOREIGN_KEY_CHECKS = 1;  commit;")
        cur.close()
        conn1.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = driver.switch_to_alert()
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


