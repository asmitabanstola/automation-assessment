from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddtoCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.search_box = (By.ID, "q")  
        self.search_button = (By.CLASS_NAME, "search-box__button--1oH7")  # Adjust if needed
        self.first_item = (By.CLASS_NAME, "qmXQo")  # first item container
        self.add_cart_button = (By.XPATH, "//div[@class='pdp-cart-concern']//button[contains(@class, 'add-to-cart-buy-now-btn') and .//span[text()='Add to Cart']]")

    def search_for_item(self, item_name):
        search_box = self.wait.until(EC.visibility_of_element_located(self.search_box))
        search_box.clear()
        search_box.send_keys(item_name)
        search_button = self.wait.until(EC.element_to_be_clickable(self.search_button))
        search_button.click()

    def select_first_item(self):
        item = self.wait.until(EC.element_to_be_clickable(self.first_item))
        item.click()

    def addition_to_cart(self):
        add_cart_btn = self.wait.until(EC.element_to_be_clickable(self.add_cart_button))
        add_cart_btn.click()
