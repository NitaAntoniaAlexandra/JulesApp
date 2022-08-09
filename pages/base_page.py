from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver import ActionChains
from time import sleep


class BasePage(Browser):

    def wait_for_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, selector)))

    def wait_and_click_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()

    def click_if_present(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        if len(elem_list) == 1:
            self.wait_and_click_elem(by, selector)

    def wait_scroll_and_click_elem(self, by, selector):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)


# in aceasta pagina punem toate metodele care sunt utile in orice pagina din proiect
# si nu sunt specifice neaparat unei singure pagini
# apoi paginile vor mosteni aceasta pagina => ca sa nu scrie de n ori wait_for_elem and other helper methods
