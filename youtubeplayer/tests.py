import unittest
import urllib
import re

class ExampleTestCase(unittest.TestCase):
    def test_url_root(self):
        url = "https://www.youtube.com/watch?v=7qFF2v8VsaA"
        query_string = urllib.parse.urlencode({"search_query": "emperors new clothes"})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        link = "http://www.youtube.com/embed/" + search_results[0];
        self.assertNotEqual(self,url,link)
