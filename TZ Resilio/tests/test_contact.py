import allure
from lib.main_page import MainPage
from lib.contact_page import ContactPage

@allure.feature("Contact us")
@allure.story("Выполнение написание предложения сайту")
def test_contact_us(browser):
    link = "http://automationpractice.com/index.php"
    page=MainPage(browser,link)
    page.open()
    page.should_be_button_contact_us()
    page.go_to_contact_us()
    contact_page=ContactPage(browser, browser.current_url)
    contact_page.should_be_contact_us_url()
    contact_page.should_be_select()
    contact_page.select_subject_heading()
    contact_page.should_be_input_mail()
    contact_page.input_mail()
    contact_page.should_be_input_order()
    contact_page.input_order()
    contact_page.should_be_file_button()
    contact_page.input_file()
    contact_page.should_be_input_message()
    contact_page.input_message()
    contact_page.should_be_button_send()
    contact_page.go_to_send()
    contact_page.should_be_url_send()
    