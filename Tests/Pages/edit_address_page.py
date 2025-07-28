from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Editaddress:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators — update these as per your app's real HTML
        self.profile_menu = (By.ID, "myAccountTrigger")  # button/menu to open address options
        self.edit_address_link = (By.XPATH, "//li[@class='account-item']/a[@id='account-popup-manage-account']")  # link to go to edit address page
        self.click_edit= (By.XPATH,"//a[@href='/address#/book' and text()='EDIT']")
        self.click_update=(By.XPATH,"//button[@type='button' and text()='EDIT' and contains(@class, 'next-btn-primary')]")
        self.landmark=(By.XPATH, "//input[@placeholder='E.g. beside train station']")
        self.save=(By.XPATH, "//button[@type='submit' and contains(@class, 'mod-address-form-btn') and text()='SAVE']")

    def open_edit_address(self):
        # Click the address menu
        profile_menu_btn = self.wait.until(EC.element_to_be_clickable(self.profile_menu))
        profile_menu_btn.click()
        
        # Click Edit address link
        edit_link = self.wait.until(EC.element_to_be_clickable(self.edit_address_link))
        edit_link.click()

        #Click Edit button
        edit_click = self.wait.until(EC.element_to_be_clickable(self.click_edit))
        edit_click.click()

        #Click update button
        update_click = self.wait.until(EC.element_to_be_clickable(self.click_update))
        update_click.click()


    def update_address(self):
        landmark_field = self.wait.until(EC.visibility_of_element_located(self.landmark))
        landmark_field.clear()
        landmark_field.send_keys("Near Metro Market")
        save_click = self.wait.until(EC.element_to_be_clickable(self.save))
        save_click.click()


        