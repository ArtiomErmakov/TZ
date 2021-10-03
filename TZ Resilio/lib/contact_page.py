from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage
from .config import ContactPageLocators
import os

class ContactPage(BasePage):
    def should_be_contact_us_url(self):
        assert self.is_element_present(*ContactPageLocators.CONTACT_US_URL),"Did not go to the contact us link"
    
    def should_be_select(self):
        assert self.is_element_present(*ContactPageLocators.SELECT_SUBJECT),"No select box"

    def select_subject_heading(self):
        select_subject=Select(self.browser.find_element(*ContactPageLocators.SELECT_SUBJECT))
        select_subject.select_by_index(1)

    def should_be_input_mail(self):
        assert self.is_element_present(*ContactPageLocators.INPUT_MAIL),"Email input field not found"
    
    def input_mail(self):
        mail = self.browser.find_element(*ContactPageLocators.INPUT_MAIL)
        mail.send_keys("artem.ermakov.000@list.ru")

    def should_be_input_order(self):
        assert self.is_element_present(*ContactPageLocators.INPUT_ORDER),"Order input field not found"
    
    def input_order(self):
        mail = self.browser.find_element(*ContactPageLocators.INPUT_ORDER)
        mail.send_keys("text")

    def should_be_file_button(self):
        assert self.is_element_present(*ContactPageLocators.BUTTON_FILE),"button file field not found"
    
    def input_file(self):
        button_file = self.browser.find_element(*ContactPageLocators.BUTTON_FILE)
        current_dir=os.path.abspath(os.path.dirname(__file__)) 
        file_path = os.path.join(current_dir, 'file.txt') 
        button_file.send_keys(file_path)

    def should_be_input_message(self):
        assert self.is_element_present(*ContactPageLocators.INPUT_MESSAGE),"Message input field not found"
    
    def input_message(self):
        message = self.browser.find_element(*ContactPageLocators.INPUT_MESSAGE)
        message.send_keys("input message")

    def should_be_button_send(self):
        assert self.is_element_present(*ContactPageLocators.BUTTON_SEND),"No button 'send'"

    def go_to_send(self):
        button_send = self.browser.find_element(*ContactPageLocators.BUTTON_SEND)
        button_send.click()

    def should_be_url_send(self):
        assert self.is_element_present(*ContactPageLocators.ALLERT_SEND),"Message not sent"

        
