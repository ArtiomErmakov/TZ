from selenium.webdriver.common.by import By
import time
from .base_page import BasePage
from .config import SignInPageLocators

class SignInPage(BasePage):
    
    def should_be_sign_in_url(self):
        assert self.is_element_present(*SignInPageLocators.SIGN_IN_URL),"Did not follow the authorization link"

    def should_be_input_mail(self):
        assert self.is_element_present(*SignInPageLocators.INPUT_MAIL),"Email input field not found"
    
    def input_mail(self):
        mail = self.browser.find_element(*SignInPageLocators.INPUT_MAIL)
        mail.send_keys("artem.ermakov.000@list.ru")

    def should_be_input_password(self):
        assert self.is_element_present(*SignInPageLocators.INPUT_PASSWORD),"Password input field not found"
    
    def input_password(self):
        password = self.browser.find_element(*SignInPageLocators.INPUT_PASSWORD)
        password.send_keys("Password")

    def should_be_sign_in_button(self):
        assert self.is_element_present(*SignInPageLocators.BUTTON_SIGN_IN),"Sign in button not found"

    def go_to_sign_in(self):
        button_sign_in = self.browser.find_element(*SignInPageLocators.BUTTON_SIGN_IN)
        button_sign_in.click()

    def should_be_button_forgot(self):
        assert self.is_element_present(*SignInPageLocators.BUTTON_FORGOT),"No button 'forgot your password?'"

    def go_to_forgot(self):
        button_forgot = self.browser.find_element(*SignInPageLocators.BUTTON_FORGOT)
        button_forgot.click()

    def should_be_input_mail_registration(self):
        assert self.is_element_present(*SignInPageLocators.INPUT_MAIL_REGISTRATION),"Email registration input field not found"
    
    def input_mail_registration(self):
        mail = self.browser.find_element(*SignInPageLocators.INPUT_MAIL_REGISTRATION)
        mail.send_keys(str(time.time()) + "@fakemail.org")

    def should_be_button_create(self):
        assert self.is_element_present(*SignInPageLocators.BUTTON_CREATE),"No button 'Create an account'"

    def go_to_create(self):
        button_create = self.browser.find_element(*SignInPageLocators.BUTTON_CREATE)
        button_create.click()