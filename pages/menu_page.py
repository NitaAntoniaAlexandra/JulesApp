from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Menu_page(BasePage):
    SEARCH_BUTTON = (By.XPATH, '//span[contains(text(),"Search")]')
    ADD_BUTTON = (By.XPATH, '//span[text()="Add"]')
    LIBRARY_BUTTON = (By.XPATH, '// span[text() = "Library"]')
    CONNECTIONS_BUTTON = (By.XPATH, '//span[contains(text(),"Connections")]')

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def click_add_button(self):
        self.driver.find_element(*self.ADD_BUTTON).click()

    def click_library_button(self):
        self.driver.find_element(*self.LIBRARY_BUTTON).click()

    def click_connections_button(self):
        self.driver.find_element(*self.CONNECTIONS_BUTTON).click()
