import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_search_text_field_max_length(self):
        search_field = self.driver.find_element_by_id("search")

    def test_search_button_enabled(self):
        search_button = self.driver.find_element_by_class_name("button")

    def test_my_account_link_is_displayed(self):
        account_link = self.driver.find_element_by_link_text("ACCOUNT")
        self.assertTrue(account_link.is_displayed())

    def test_account_links(self):
        account_links = self.driver.find_element_by_partial_link_text("ACCOUNT")
        self.assertTrue(2, len(account_links))

