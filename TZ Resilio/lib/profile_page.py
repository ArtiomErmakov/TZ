from selenium.webdriver.common.by import By
from .base_page import BasePage
from .config import ProfilePageLocators

class ProfilePage(BasePage):
    def should_be_account(self):
        assert self.is_element_present(*ProfilePageLocators.ACCOUNT),"Login failed"

    def go_to_sign_out(self):
        button_sign_out = self.browser.find_element(*ProfilePageLocators.BUTTON_SIGN_OUT)
        button_sign_out.click()

    def should_be_button_sign_out(self):
        assert self.is_element_present(*ProfilePageLocators.BUTTON_SIGN_OUT),"No button Sign OUT"
    