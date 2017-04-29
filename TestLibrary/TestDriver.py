import MySQLdb
import csv
import unittest
from selenium import webdriver
from login.Data import LoginDataGenerate


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
        conn1 = MySQLdb.connect(host = "localhost", user = "root", passwd = "40OZlike", db = "plalyst")
        cur = conn1.cursor()
        conn1.set_character_set('utf8')
        cur.execute('SET NAMES utf8;')
        cur.execute('SET CHARACTER SET utf8;')
        cur.execute('SET character_set_connection=utf8;')
        cur.execute("insert into login_playlist (Plalyst_title,user_id) values('test_pl',1)")
        cur.execute("commit")
        cur.execute("select id from login_playlist where Plalyst_title= 'test_pl'")
        pl_id=cur.fetchall()[0][0]
        with open('TestLibrary/TestData2.csv', 'rt',encoding='UTF-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='"', quotechar='|')
            for row in spamreader:
                curry = 'insert into login_song (song_title,playlist_id) values("'+row[0]+'",'+str(pl_id)+')'
                cur.execute(curry)
                cur.execute("commit")
        driver.find_element_by_xpath("(//a[contains(text(),'Generate Recommendations')])[2]").click()
        res = driver.find_element_by_css_selector("ul > a")
        link = res.get_attribute("href")
        self.assertNotEqual(link, 'http://localhost:8000/generate/1/(ii)%20Falter/')
        driver.find_element_by_link_text('Logout').click()
        cur.execute("delete from login_song where login_song.playlist_id in ( select id from login_playlist where Plalyst_title = 'test_pl')")
        cur.execute("commit")
        cur.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cur.execute("delete from login_playlist where Plalyst_title = 'test_pl'")
        cur.execute("SET FOREIGN_KEY_CHECKS = 1;")
        cur.execute("commit")
        cur.close()
        conn1.close()
if __name__ == "__main__":
    unittest.main()
