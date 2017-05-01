from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from login.forms import PlaylistForm, SongForm, UserForm
from django.test.client import Client
from .Data import PlaylistName, inputSong, LoginDataGenerate, RegisterDetails
import re,time,urllib,MySQLdb,unittest
import csv
from TestLibrary.Parser import filepref


class GeneratePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_generate_playlist(self):
        print("Generate Playlist")
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
        print("Create Song")
        songList=inputSong()
        driver = self.driver
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("View Details").click()
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
        print("Youtube")
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


class FormTests(unittest.TestCase):
    def test_form1(self):
        print("FormTests")
        form_data = {'song_title': inputSong()}
        form = SongForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forms(self):
        print("FormTests1")
        form_data = {'Plalyst_title': PlaylistName()}
        form = PlaylistForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_user_data(self):
        user = LoginDataGenerate()
        user1 = RegisterDetails()
        form_data = {'username': user.name,
                     'email': user1.name,
                     'password': user1.password}
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())




class URL(unittest.TestCase):
    def test_url(self):
        print("url")
        client = Client()
        response = client.get('http://localhost:8000/generate/1/')
        self.assertEqual(response.status_code, 200)


class YoutubeLinkTestCase(unittest.TestCase):
    def test_url_root(self):
        print("YT link test case")
        url = "http://www.youtube.com/embed/7qFF2v8VsaA"
        query_string = urllib.parse.urlencode({"search_query": "emperors new clothes"})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        link = "http://www.youtube.com/embed/" + search_results[0]
        self.assertEqual(url, link)


class PrefChangeRec(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_pref_change_rec(self):
        driver = self.driver
        with open('TestLibrary/' + filepref) as csvfile:
            preferences = csv.reader(csvfile, delimiter='"', quotechar='|')
            preferencelist=[]
            for row in preferences:
                preferencelist.append(row)
        user = LoginDataGenerate()
        driver.get(self.base_url + "login/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(user.name)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys(user.password)
        driver.find_element_by_css_selector("button.btn.btn-success").click()
        driver.find_element_by_link_text("Generate Recommendations").click()
        time.sleep(10)
        list_of_links1 = driver.find_elements_by_tag_name("a")
        recomm1=''
        for link1 in list_of_links1:
            recomm1+=(link1.get_attribute('text'))
        driver.find_element_by_link_text("profiles").click()
        driver.find_element_by_link_text("View Details").click()
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
        driver.find_element_by_link_text("Generate Recommendations").click()
        time.sleep(10)
        list_of_links2 = driver.find_elements_by_tag_name("a")
        recomm2 = ''
        for link2 in list_of_links2:
            recomm2 += (link2.get_attribute('text'))
        self.assertNotEqual(recomm1,recomm2)
        driver.find_element_by_link_text('Logout').click()
        conn1 = MySQLdb.connect(host="localhost", user="root", passwd="40OZlike", db="plalyst")
        cur = conn1.cursor()
        cur.execute('delete from login_addpreferences; COMMIT ;')
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
