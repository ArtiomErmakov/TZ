from selenium.webdriver.common.by import By
from .base_page import BasePage
from .config import ForgotPageLocators

class ForgotPage(BasePage):
    def should_be_forgot_your_password(self):
        assert self.is_element_present(*ForgotPageLocators.FORGOT_TEG),"Didn't switch to password recovery"

    def input_mail(self):
        mail = self.browser.find_element(*ForgotPageLocators.INPUT_MAIL)
        mail.send_keys("artem.ermakov.000@list.ru")

    def should_be_input_mail(self):
        assert self.is_element_present(*ForgotPageLocators.INPUT_MAIL),"Email input field not found"

    def should_be_retrieve_button(self):
        assert self.is_element_present(*ForgotPageLocators.BUTTON_RETRIEVE),"Retrieve password button not found"

    def go_to_retrieve(self):
        button_retrieve = self.browser.find_element(*ForgotPageLocators.BUTTON_RETRIEVE)
        button_retrieve.click()

    def should_be_url_retrieve(self):
        assert self.is_element_present(*ForgotPageLocators.ALLERT_RETRIEVE_PASSWORD),"Confirmation email not sent"
