from django.test import LiveServerTestCase
from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#import time
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


class UsersCanFindWebPages(unittest.TestCase):
    # run locally at 'http://127.0.0.1:8000/'
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_find_home_page(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Home | DjangoPlay2Learn', self.browser.title)

    def test_can_find_contact_page(self):
        self.browser.get('http://127.0.0.1:8000/contact/')
        self.assertIn('Contact | DjangoPlay2Learn', self.browser.title)

    def test_can_find_gamescores_page(self):
        self.browser.get('http://127.0.0.1:8000/game-scores/')
        self.assertIn('Game Scores | DjangoPlay2Learn', self.browser.title)

    def test_can_find_games_page(self):
        self.browser.get('http://127.0.0.1:8000/games/')
        self.assertIn('Games | DjangoPlay2Learn', self.browser.title)

    def test_can_find_myscores_page(self):
        self.browser.get('http://127.0.0.1:8000/myscores/')
        self.assertIn('My Scores | DjangoPlay2Learn', self.browser.title)

    def test_can_find_reviews_page(self):
        self.browser.get('http://127.0.0.1:8000/review/review/')
        self.assertIn('Reviews | DjangoPlay2Learn', self.browser.title)

    def test_can_find_login_page(self):
        self.browser.get('http://127.0.0.1:8000/accounts/login/')
        self.assertIn('Log in | DjangoPlay2Learn', self.browser.title)

    def test_can_find_registration_page(self):
        self.browser.get('http://127.0.0.1:8000/accounts/signup/')
        self.assertIn('Register | DjangoPlay2Learn', self.browser.title)

#def test_can_access_site(self):
    #self.browser.get(self.live_server_url)
"""

class ContactPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_submit_contact_form(self):
        self.browser.get('http://127.0.0.1:8000/contact/')
        self.assertIn('Contact | DjangoPlay2Learn', self.browser.title)
        email = webdriver.find_element_by_id('id_email')
        email.send_keys('Test Email')
        subject = self.browser.find_element_by_id('id_subject')
        subject.send_keys('Test Subject')
        message = self.browser.find_element_by_id('id_message')
        message.send_keys('This email is a test.')
        submit = self.browser.find_element_by_id('submit_contact_form')
        submit.send_keys(Keys.ENTER)


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
