from selenium import webdriver
import unittest


class WorksInFirefoxTest(unittest.TestCase):
    # run locally at 'http://127.0.0.1:8000/'
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_website_runs_on_firefox(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Home | DjangoPlay2Learn', self.browser.title)


class WorksInChromeTest(unittest.TestCase):
    # run locally at 'http://127.0.0.1:8000/'
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_website_runs_on_chrome(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Home | DjangoPlay2Learn', self.browser.title)

"""

class WorksInSafariTest(unittest.TestCase):
    # run locally at 'http://127.0.0.1:8000/'

    selenium.common.exceptions.SessionNotCreatedException: Message: Could not create a session: You must enable the 'Allow Remote Automation' option in Safari's Develop menu to control Safari via WebDriver.


    def setUp(self):
        self.browser = webdriver.Safari()

    def tearDown(self):
        self.browser.quit()

    def test_website_runs_on_safari(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Home | DjangoPlay2Learn', self.browser.title)
"""

if __name__ == '__main__':
    unittest.main()
