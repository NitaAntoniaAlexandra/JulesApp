from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Add_page(BasePage):
    PROPERTY = (By.XPATH, '//span[text()="Add a property to your Jules account."]')

    def click_property(self):
        self.driver.find_element(*self.PROPERTY).click()
