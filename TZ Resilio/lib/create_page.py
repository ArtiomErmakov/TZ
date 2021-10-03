from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from .base_page import BasePage
from .config import CreatePageLocators

class CreatePage(BasePage):
    def should_be_create_url(self):
        assert self.is_element_present(*CreatePageLocators.CREATE_URL),"No transition to the registration page"
    
    def should_be_radiobutton_gender(self):
        assert self.is_element_present(*CreatePageLocators.RADIO_GENDER),"Gender button not found"
    
    def radiobutton_gender(self):
        gender = self.browser.find_element(*CreatePageLocators.RADIO_GENDER)
        gender.click()

    def should_be_input_first_name(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_FIRST_NAME),"first name input field not found"
    
    def input_first_name(self):
        first_name = self.browser.find_element(*CreatePageLocators.INPUT_FIRST_NAME)
        first_name.send_keys("Artyom")

    def should_be_input_last_name(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_LAST_NAME),"last name input field not found"
    
    def input_last_name(self):
        last_name = self.browser.find_element(*CreatePageLocators.INPUT_LAST_NAME)
        last_name.send_keys("Ermakov")

    def should_be_input_mail(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_MAIL),"mail input field not found"
    
    def input_mail(self):
        mail = self.browser.find_element(*CreatePageLocators.INPUT_MAIL)
        mail.click()

    def should_be_input_password(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_PASSWORD),"password input field not found"
    
    def input_password(self):
        password = self.browser.find_element(*CreatePageLocators.INPUT_PASSWORD)
        password.send_keys("Password")

    def should_be_select_days(self):
        assert self.is_element_present(*CreatePageLocators.SELECT_DAYS),"select days field not found"
    
    def select_days(self):
        days = Select(self.browser.find_element(*CreatePageLocators.SELECT_DAYS))
        days.select_by_value("12")

    def should_be_select_month(self):
        assert self.is_element_present(*CreatePageLocators.SELECT_MONTH),"select month field not found"
    
    def select_month(self):
        month = Select(self.browser.find_element(*CreatePageLocators.SELECT_MONTH))
        month.select_by_index(10)

    def should_be_select_year(self):
        assert self.is_element_present(*CreatePageLocators.SELECT_YEAR),"select days field not found"
    
    def select_year(self):
        year = Select(self.browser.find_element(*CreatePageLocators.SELECT_YEAR))
        year.select_by_value("1999")

    def should_be_checkbutton_sign(self):
        assert self.is_element_present(*CreatePageLocators.CHECK_SIGN),"sign button not found"
    
    def checkbutton_sign(self):
        sign = self.browser.find_element(*CreatePageLocators.CHECK_SIGN)
        sign.click()

    def should_be_checkbutton_receive(self):
        assert self.is_element_present(*CreatePageLocators.CHECH_RECEIVE),"Receive button not found"
    
    def checkbutton_receive(self):
        receive = self.browser.find_element(*CreatePageLocators.CHECH_RECEIVE)
        receive.click()

    def should_be_input_firstname(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_FNAME),"firstname input field not found"
    
    def input_firstname(self):
        first_name = self.browser.find_element(*CreatePageLocators.INPUT_FNAME)
        first_name.click()

    def should_be_input_lastname(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_LNAME),"lastname input field not found"
    
    def input_lastname(self):
        last_name = self.browser.find_element(*CreatePageLocators.INPUT_LNAME)
        last_name.click()

    def should_be_input_company(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_COMPANY),"company input field not found"
    
    def input_company(self):
        company = self.browser.find_element(*CreatePageLocators.INPUT_COMPANY)
        company.send_keys("Resilio")

    def should_be_input_address(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_ADDRESS),"address input field not found"
    
    def input_address(self):
        address = self.browser.find_element(*CreatePageLocators.INPUT_ADDRESS)
        address.send_keys("Vera Horuzhei street 25/3")

    def should_be_input_address_dop(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_ADDRESS2),"address input field not found"
    
    def input_address_dop(self):
        address = self.browser.find_element(*CreatePageLocators.INPUT_ADDRESS2)
        address.send_keys("8th floor")

    def should_be_input_city(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_CITY),"city input field not found"
    
    def input_address_city(self):
        city = self.browser.find_element(*CreatePageLocators.INPUT_CITY)
        city.send_keys("Minsk")

    def should_be_select_state(self):
        assert self.is_element_present(*CreatePageLocators.SELECT_STATE),"select state field not found"
    
    def select_state(self):
        state = Select(self.browser.find_element(*CreatePageLocators.SELECT_STATE))
        state.select_by_index(5)

    def should_be_input_index(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_INDEX),"index input field not found"
    
    def input_address_index(self):
        index = self.browser.find_element(*CreatePageLocators.INPUT_INDEX)
        index.send_keys("21141")

    def should_be_textarea(self):
        assert self.is_element_present(*CreatePageLocators.TEXTAREA),"Additional information field not found"
    
    def textarea_input(self):
        textarea = self.browser.find_element(*CreatePageLocators.TEXTAREA)
        textarea.send_keys("Additional information absent")

    def should_be_input_home_telefon(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_HOME_TELEFON),"home telefon input field not found"
    
    def input_home_telefon(self):
        telefon = self.browser.find_element(*CreatePageLocators.INPUT_HOME_TELEFON)
        telefon.send_keys("-")
            
    def should_be_input_mobile_telefon(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_MOBILE_TELEFON),"mobile telefon input field not found"
    
    def input_mobile_telefon(self):
        telefon = self.browser.find_element(*CreatePageLocators.INPUT_MOBILE_TELEFON)
        telefon.send_keys("+375333292419")

    def should_be_input_name_on_site(self):
        assert self.is_element_present(*CreatePageLocators.INPUT_NAME_IN_SITE),"Assign an address alias for future reference input field not found"
    
    def input_name_on_site(self):
        name = self.browser.find_element(*CreatePageLocators.INPUT_NAME_IN_SITE)
        self.browser.execute_script("arguments[0].value=arguments[1];", name,  "6ylka99"+"\ue007")
        
    def should_be_button_register(self):
        assert self.is_element_present(*CreatePageLocators.BUTTON_REGISTER),"register button not found"
    
    def button_register(self):
        register = self.browser.find_element(*CreatePageLocators.BUTTON_REGISTER)
        register.click()