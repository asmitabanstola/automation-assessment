import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.login_page import LoginPage
from Pages.edit_address_page import Editaddress

def edit_address_test():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.page_load_strategy = 'eager'

    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Login
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.enter_username(os.getenv('DARAZ_USERNAME'))
        login_page.enter_password(os.getenv('DARAZ_PASSWORD'))
        login_page.click_login()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "myAccountTrigger"))
        )
        print("Login successful")

        # Open Edit addresmenus page
        edit_address_page = Editaddress(driver)
        edit_address_page.open_edit_address()

        #Update menu details
        edit_address_page.update_address()
        print("Address Updated")

    finally:
        driver.quit()


if __name__ == "__main__":
    edit_address_test()
