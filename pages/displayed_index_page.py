from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Displayedl_index_page(BasePage):
    SEARCH_FIELD = (By.XPATH, '//input[@placeholder="Type and Search..."]')
    FILTER_BUTTON = (By.XPATH, '//span[contains(text(),"FILTER")]')
    LIBRARY = (By.XPATH, '// span[text() = "Library"]')
    RECORD_BUTTON = (By.XPATH, '//li[contains(text(),"Record")]')
    DELETE_BUTTON = (By.XPATH, '//div[button="Delete"]')
    ERROR_MESSAGE = (By.XPATH, '//span[contains(text(), "Please")]')
    EXIT_SEARCH_FIELD_BUTTON = (By.XPATH, '//div[@class="jss93"]//button')


    def fill_search_field(self):
        self.driver.find_element(*self.SEARCH_FIELD).send_keys().send_keys(Keys.ENTER)
        sleep(2)

    def click_filter_button(self):
        self.driver.find_element(*self.FILTER_BUTTON).click()

    def click_record_button(self):
        self.driver.find_element(*self.RECORD_BUTTON).click()
        self.driver.find_element(By.XPATH, '//span[contains(text(), "Estate")]').click()

    def click_delete_button(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()

    def verify_displayed_error_message(self):
        delete_error = self.driver.find_element(*self.ERROR_MESSAGE)
        self.assertTrue(delete_error.is_displayed(), 'No error message')

    def click_ok_button(self):
        self.driver.find_element(By.XPATH, '//span[contains(text(), "OK")]').click()

    def verify_correct_page(self):
        actual = self.driver.current_url
        expected = 'https://jules.app/search/all?displayIndex[0]=record&recordId[0]=4475'
        self.assertEqual(actual, expected, 'URL is incorrect.')

    def click_exit_search(self):
        self.driver.find_element(*self.EXIT_SEARCH_FIELD_BUTTON).click()
