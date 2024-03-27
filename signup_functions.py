# signup_functions.py
import logging
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class SignUpFunctions:
    def __init__(self,driver):
        self.driver=driver
     
    def find_element_by_xpath_and_send_keys(self, xpath, keys):
        element =self. driver.find_element(By.XPATH, xpath)
        element.send_keys(keys)
        time.sleep(4)

    def find_element_by_xpath_and_click(self, xpath):
        next_button = self.driver.find_element(By.XPATH, xpath)
        next_button.click()
        logging.info("Clicked element with xpath: %s", xpath)
        time.sleep(4)
