from selenium.webdriver.common.by import By


class MainPageLocators():
    BUTTON_SIGN_IN = (By.CLASS_NAME, "login")
    BUTTON_SIGN_OUT = (By.CSS_SELECTOR, "a.logout")
    BUTTON_CONTACT_US =(By.CSS_SELECTOR, "[title='Contact Us']")
    

class SignInPageLocators():
	SIGN_IN_URL = (By.TAG_NAME, "h1")
	INPUT_MAIL = (By.ID, "email")
	INPUT_PASSWORD = (By.ID, "passwd")
	BUTTON_SIGN_IN = (By.ID, "SubmitLogin")
	BUTTON_FORGOT = (By.XPATH , "//*[@id='login_form']/div/p[1]/a")
	INPUT_MAIL_REGISTRATION = (By.ID, "email_create")
	BUTTON_CREATE = (By.ID, "SubmitCreate")


class ProfilePageLocators():
	ACCOUNT = (By.TAG_NAME, "h1")
	BUTTON_SIGN_OUT = (By.CSS_SELECTOR, "a.logout")


class ForgotPageLocators():
	FORGOT_TEG = (By.TAG_NAME, "h1")
	INPUT_MAIL = (By.ID, "email")
	BUTTON_RETRIEVE = (By.CSS_SELECTOR, "button.btn.btn-default.button.button-medium")
	ALLERT_RETRIEVE_PASSWORD=(By.CSS_SELECTOR, "p.alert.alert-success") 


class ContactPageLocators():
	CONTACT_US_URL = (By.TAG_NAME, "h1")
	SELECT_SUBJECT = (By.ID, "id_contact")
	INPUT_MAIL = (By.ID, "email")
	INPUT_ORDER = (By.ID, "id_order")
	BUTTON_FILE = (By.ID, "fileUpload")
	INPUT_MESSAGE = (By.ID, "message")
	BUTTON_SEND = (By.ID, "submitMessage")
	ALLERT_SEND=(By.CSS_SELECTOR, "p.alert.alert-success") 


class CreatePageLocators():
	CREATE_URL = (By.CSS_SELECTOR, "h3.page-subheading")
	RADIO_GENDER = (By.ID, "id_gender1")
	INPUT_FIRST_NAME = (By.ID, "customer_firstname")
	INPUT_LAST_NAME = (By.ID, "customer_lastname")
	INPUT_MAIL = (By.ID, "email")
	INPUT_PASSWORD = (By.ID, "passwd")
	SELECT_DAYS = (By.ID, "days")
	SELECT_MONTH = (By.ID, "months")
	SELECT_YEAR = (By.ID, "years")
	CHECK_SIGN = (By.ID, "newsletter")
	CHECH_RECEIVE = (By.ID, "optin")
	INPUT_FNAME = (By.ID, "firstname")
	INPUT_LNAME = (By.ID, "lastname")
	INPUT_COMPANY = (By.ID, "company")
	INPUT_ADDRESS = (By.ID, "address1")
	INPUT_ADDRESS2 = (By.ID, "address2")
	INPUT_CITY = (By.ID, "city")
	SELECT_STATE = (By.ID, "id_state")
	INPUT_INDEX = (By.ID, "postcode")
	TEXTAREA = (By.TAG_NAME, "textarea")
	INPUT_HOME_TELEFON = (By.ID, "phone")
	INPUT_MOBILE_TELEFON = (By.ID, "phone_mobile")
	INPUT_NAME_IN_SITE = (By.ID, "alias")
	BUTTON_REGISTER = (By.ID, "submitAccount")