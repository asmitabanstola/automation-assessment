from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login = (By.ID, "anonLogin")
        self.username_textbox = (By.XPATH, "//input[@placeholder='Please enter your Phone or Email']")
        self.password_textbox = (By.XPATH, "//input[@class='iweb-input' and @type='password']")
        self.login_button = (By.XPATH, "//button[contains(text(), 'LOGIN')]")
        self.wait = WebDriverWait(driver, 30)

    def open_login_page(self):
        self.driver.get("https://www.daraz.com.np/")
        self.wait.until(EC.element_to_be_clickable(self.login)).click()

    def enter_username(self, username):
        username_input = self.wait.until(EC.visibility_of_element_located(self.username_textbox))
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located(self.password_textbox))
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button.click()
