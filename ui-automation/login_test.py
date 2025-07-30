import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.login_page import LoginPage

def test_login():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.page_load_strategy = 'eager'

    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        login_page = LoginPage(driver)
        login_page.open_login_page()  # This method should navigate to base URL internally

        username = os.getenv('DARAZ_USERNAME')
        password = os.getenv('DARAZ_PASSWORD')

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()

        exp = "//*[@id='myAccountTrigger' and contains(translate(text(),'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'), 'account')]"
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, exp))
            )
            print("Login Successful")
        except TimeoutException:
            print("Login Failure")

    finally:
        driver.quit()


def test_invalid_login():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.page_load_strategy = 'eager'

    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        login_page = LoginPage(driver)
        login_page.open_login_page()

        # Use invalid username and password
        invalid_username = "test@example.com"
        invalid_password = "password123"

        login_page.enter_username(invalid_username)
        login_page.enter_password(invalid_password)
        login_page.click_login()

        try:
            toast = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "iweb-toast-wrap"))
            )
            if "Invalid account or password" in toast.text:
                print(" Login failed — invalid credentials.")
        except:
            print("⚠️ No toast message appeared (maybe login succeeded or toast timed out).")

    finally:
        driver.quit()

if __name__ == '__main__':
    test_login() # valid credential
    test_invalid_login()  # Test invalid credentials
