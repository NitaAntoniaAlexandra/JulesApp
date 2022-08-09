from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Sign_in_page(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Enter your password"]')
    LOGIN_BUTTON = (By.XPATH, '//span[text() = "Log in"]/parent::button')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[@href ="/forgot-password"]')

    def navigate_to_sigin_page(self):
        self.driver.get('https://jules.app/sign-in')

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        sleep(3)

    def user_login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()
