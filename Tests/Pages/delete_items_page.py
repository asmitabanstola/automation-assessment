from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteItems:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.cart_icon = (By.XPATH, "//div[@class='lzd-nav-cart']/a[@href='https://cart.daraz.com.np/cart']")
        self.cart_icon_span = (By.CSS_SELECTOR, "div.lzd-nav-cart > a > span.cart-icon-daraz")
        self.delete_button = (By.XPATH, "//span[@class='lazada lazada-ic-Delete lazada-icon icon delete']")
        self.confirm_delete_button = (By.XPATH, "//button[text()='REMOVE']")

    def open_cart(self):
        # Wait for the cart container presence
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'lzd-nav-cart')))

        # Wait until cart icon span is visible (the SVG icon)
        cart_icon_span = self.wait.until(EC.visibility_of_element_located(self.cart_icon_span))

        # Wait until the <a> tag is clickable
        cart_link = self.wait.until(EC.presence_of_element_located(self.cart_icon))

        try:
            # Check if the cart link has size before clicking
            if cart_link.size['height'] > 0 and cart_link.size['width'] > 0:
                cart_link.click()
            else:
                # If size is zero, fallback to JS click on span icon
                self.driver.execute_script("arguments[0].click();", cart_icon_span)
        except Exception:
            # If normal click fails, fallback to JS click on the link
            self.driver.execute_script("arguments[0].click();", cart_link)

    def delete_first_item(self):
        delete_btn = self.wait.until(EC.element_to_be_clickable(self.delete_button))
        delete_btn.click()

        confirm_btn = self.wait.until(EC.element_to_be_clickable(self.confirm_delete_button))
        confirm_btn.click()
