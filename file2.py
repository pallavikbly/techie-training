# file2.py

import logging
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

from signup_functions import SignUpFunctions
# Import the functions from signup_functions.py

logging.basicConfig(level=logging.INFO, filename='signup.log', format='%(asctime)s - %(levelname)s - %(message)s')

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://accounts.google.com/signup")
logging.info("Signup page is opened")
time.sleep(4)

try:
    sign_up=SignUpFunctions(driver)

    sign_up.find_element_by_xpath_and_send_keys('//*[@id="firstName"]', "Varnika")
    logging.info("Entered first name")
    
    sign_up.find_element_by_xpath_and_send_keys('//*[@id="lastName"]', "Arya")
    logging.info("Entered last name")
    sign_up.find_element_by_xpath_and_click('//*[@id="collectNameNext"]/div/button/span')

    month = driver.find_element(By.XPATH, '//*[@id="month"]')
    select_month = Select(month)
    select_month.select_by_visible_text("May")
    logging.info("Selected month")
    time.sleep(4)

    sign_up.find_element_by_xpath_and_send_keys('//*[@id="day"]', "11")
    logging.info("Entered day")

    sign_up.find_element_by_xpath_and_send_keys('//*[@id="year"]', "1991")
    logging.info("Entered year")

    gender = driver.find_element(By.XPATH, '//*[@id="gender"]')
    select_gender = Select(gender)
    select_gender.select_by_visible_text("Female")
    logging.info("Selected gender")
    time.sleep(4)

    sign_up.find_element_by_xpath_and_click('//*[@id="birthdaygenderNext"]/div/button/span')

    radio_button = driver.find_element(By.XPATH, "(//div)[48]")
    radio_button.click()
    logging.info("Clicked radio button to select Gmail ID")
    time.sleep(3)

    sign_up.find_element_by_xpath_and_click('//*[@id="next"]/div/button/span')

    sign_up.find_element_by_xpath_and_send_keys('//*[@id="passwd"]/div[1]/div/div[1]/input', "Varnika@123")
    logging.info("Entered password")

    sign_up.find_element_by_xpath_and_send_keys('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input',
                                                          "Varnika@123")
    logging.info("Entered confirm password")

    sign_up.find_element_by_xpath_and_click('//*[@id="createpasswordNext"]/div/button/span')

    sign_up.find_element_by_xpath_and_send_keys('//*[@id="phoneNumberId"]', "9986866435")
    logging.info("Entered phone number")

    sign_up.find_element_by_xpath_and_click(
                                                  '//*[@id="yDmH0d"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]/div/div/button/span')

except TimeoutException:
    logging.error("Timeout: Element not found within the specified time.")
except NoSuchElementException:
    logging.error("Element not found on the page.")
except ElementClickInterceptedException:
    logging.error("Element Click Intercepted Exception")
finally:
    driver.quit()
