from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Search_all_page(BasePage):
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Type and Search..."]')
    FILTER_BUTTON = (By.XPATH, '//span[contains(text(),"FILTER")]')
    LIBRARY = (By.XPATH, '// span[text() = "Library"]')
    RECORD_BUTTON = (By.XPATH, '//li[contains(text(),"Record")]')

    def fill_search_field_click_enter(self):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys().send_keys(Keys.ENTER)
        sleep(2)

    def click_filter_button(self):
        self.driver.find_element(*self.FILTER_BUTTON).click()

    def click_record_button(self):
        self.driver.find_element(*self.RECORD_BUTTON).click()


    def click_testing_jules_app_real_estate(self):
        self.driver.find_element(By.XPATH,'//span[contains(text(),"Estate")]').click()


    def verify_correct_page(self):
        actual = self.driver.current_url
        expected = 'https://jules.app/search/all'
        self.assertEqual(actual, expected, 'URL is incorrect.The login process is not successful.')
