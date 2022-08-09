from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Add_property_page(BasePage):
    PROPERTY_NICKNAME = (By.XPATH, '//input[@type="text"]')
    CONTINUE_BUTTON = (By.XPATH, '//span[contains(text(), "Continue")]/parent::button/parent::div')
    ADDRESS = (By.XPATH, '//label[contains(text(), "Address")]/parent::div//div//input"]')
    SAVE_PROPERTY_BUTTON = (By.XPATH, '//span[contains(text(), "Save")]')
    SUCCES_MESSAGE = (By.XPATH, '//span[contains(text(), "successfully")]')
    FINISH_BUTTON = (By.XPATH, '//span[contains(text(), "Finish")]')
    NO_THANKS_BUTTON = (By.XPATH, '//button[contains(text(),"No Thanks")]')

    def set_property_nickname(self, name):
        self.driver.find_element(*self.PROPERTY_NICKNAME).send_keys(name)
        sleep(2)

    def click_continue_button(self):
        #self.driver.find_element(*self.CONTINUE_BUTTON).click()
        self.driver.find_element(*self.PROPERTY_NICKNAME).send_keys(Keys.ENTER)
        sleep(2)

    def fill_property_address(self):
        self.driver.find_element(*self.ADDRESS).send_keys()

    # def click_save_button(self):
    #     button = self.driver.find_element(*self.SAVE_PROPERTY_BUTTON)
    #     button.location_once_scrolled_into_view
    #     button.click()
    def click_save_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(*self.SAVE_PROPERTY_BUTTON))
        elem = self.driver.find_element(By.XPATH, '//span[contains(text(), "Save")]')
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    #def wait_and_click_elem(self, by, selector):
    #    WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(*self.NO_THANKS_BUTTON))
     #   self.driver.find_element(self.NO_THANKS_BUTTON).click()

    def verify_success_message(self):
        message = self.driver.find_element(*self.SUCCES_MESSAGE).text
        self.assertTrue(message.is_displayed(), 'The message is not displayed!')


    def click_if_present(self,  by, selector):
       elem_list = self.driver.find_elements(By.XPATH, '//button[contains(text(),"No Thanks")]')
       if len(elem_list) == 1:
           self.wait_and_click_elem(By.XPATH, '//button[contains(text(),"No Thanks")]')

    def click_finish_button(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
