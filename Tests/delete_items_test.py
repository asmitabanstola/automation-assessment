from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from Pages.delete_items_page import DeleteItems
from Pages.add_to_cart_page import AddtoCartPage
from Pages.login_page import LoginPage
from Pages.search_page import SearchPage
from Pages.add_to_cart_page import AddtoCartPage

def add_and_delete():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    chrome_options.page_load_strategy = 'eager'

    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # === LOGIN ===
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.enter_username(os.getenv('DARAZ_USERNAME'))
        login_page.enter_password(os.getenv('DARAZ_PASSWORD'))
        login_page.click_login()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myAccountTrigger"))
        )
        print("Login Successful")

        # === SEARCH & ADD TO CART ===
        search_page = SearchPage(driver)
        search_page.search_for_item("Erke fleece jacket")
        print("Search completed")

        add_to_cart_page = AddtoCartPage(driver)
        add_to_cart_page.select_first_item()
        add_to_cart_page.addition_to_cart()
        print("Item added to cart")

        # === DELETE FROM CART ===
        delete_cart_page = DeleteItems(driver)
        delete_cart_page.open_cart()
        delete_cart_page.delete_first_item()
        print("Item deleted from cart")

    finally:
        driver.quit()


if __name__ == "__main__":
    add_and_delete()
