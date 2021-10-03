from selenium.webdriver.common.by import By
from .base_page import BasePage
from .config import MainPageLocators

class MainPage(BasePage):
    def go_to_sign_in(self):
        button_sign_in = self.browser.find_element(*MainPageLocators.BUTTON_SIGN_IN)
        button_sign_in.click()
    
    def should_be_button_sign_in(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_SIGN_IN),"No button Sign In"
        
    def should_not_be_button_sign_out(self):
        assert self.is_not_element_present(*MainPageLocators.BUTTON_SIGN_OUT),"the logout button was found, although it shouldn't"    
    
    def go_to_sign_out(self):
        button_sign_out = self.browser.find_element(*MainPageLocators.BUTTON_SIGN_OUT)
        button_sign_out.click()

    def go_to_contact_us(self):
        button_sign_in = self.browser.find_element(*MainPageLocators.BUTTON_CONTACT_US)
        button_sign_in.click()
    
    def should_be_button_contact_us(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_CONTACT_US),"No button Contact us"