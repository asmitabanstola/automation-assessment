from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.base_url = 'https://www.daraz.com.np/'
        self.search_box_locator = (By.NAME, 'q')  # confirm this matches site
        self.search_button_locator = (By.CLASS_NAME, 'search-box__button--1oH7')
        self.product_titles_locator = (By.CLASS_NAME, 'RfADt')

    def open(self):
        self.driver.get(self.base_url)

    def enter_search_term(self, term):
        search_box = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(self.search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(term)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.search_button_locator)
        )
        search_button.click()

    def get_product_titles(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(self.product_titles_locator)
        )
        products = self.driver.find_elements(*self.product_titles_locator)
        return [product.text for product in products]

    # New helper method for convenience
    def search_for_item(self, term):
        self.open()
        self.enter_search_term(term)
        self.click_search_button()
