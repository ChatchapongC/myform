from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from urllib import response, request
from urllib.error import URLError, HTTPError
import time

class TestSerenium(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Users/mac/Desktop/chromedriver")

    def login_test(self):
        """
        Test Login with username and password and check that in this page have both "Login,Sign Up" words.
        After,go to next page(event).
        """
        user = "Jirawadee2"
        password = "test12345"
        self.driver.get('http://127.0.0.1:8000/')
        
        userBar = self.driver.find_element_by_id('user')
        passwordBar = self.driver.find_element_by_id('pass')

        userBar.send_keys(user)
        passwordBar.send_keys(password)

        
        self.assertIn('Login',self.driver.page_source)
        self.assertIn('Sign Up',self.driver.page_source)

        submitButton = self.driver.find_element_by_id("submit")
        submitButton.click()


        self.assertIn('event',self.driver.current_url)
        print(self.driver.current_url)

        self.driver.quit()


    def event_test(self):
        """
        Test Login with username and password and check that in this page have both "Login,Sign Up" words.
        After,go to next page(event).
        """
        user = "Jirawadee2"
        password = "test12345"
        self.driver.get('http://127.0.0.1:8000/')
        
        userBar = self.driver.find_element_by_id('user')
        passwordBar = self.driver.find_element_by_id('pass')
        
        userBar.send_keys(user)
        passwordBar.send_keys(password)

        submitButton = self.driver.find_element_by_id("submit")
        submitButton.click()

        self.assertIn('Even List',self.driver.page_source)
        self.assertIn('My Event',self.driver.page_source)

        eventButton = self.driver.find_element_by_id("create")
        eventButton.click()

        self.driver.quit()
 
    def create_test(self):
        """
        Test Login with username and password and check that in this page have both "Login,Sign Up" words.
        After,go to next page(event).
        """
        user = "Jirawadee2"
        password = "test12345"
        self.driver.get('http://127.0.0.1:8000/')
        
        userBar = self.driver.find_element_by_id('user')
        passwordBar = self.driver.find_element_by_id('pass')
        
        userBar.send_keys(user)
        passwordBar.send_keys(password)

        submitButton = self.driver.find_element_by_id("submit")
        submitButton.click()

        eventButton = self.driver.find_element_by_id("create")
        eventButton.click()
        
        self.assertIn('Even Name',self.driver.page_source)
        self.assertIn('Question',self.driver.page_source)

        createButton = self.driver.find_element_by_id("eventname")
        createButton.click()
        
        self.driver.quit()



if __name__ == "__main__":
    test = TestSerenium()
    test.setUp()
    test.login_test()
    test.setUp()
    test.event_test()
    test.setUp()
    test.create_test()