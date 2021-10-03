import allure
from lib.main_page import MainPage
from lib.sign_in_page import SignInPage
from lib.forgot_page import ForgotPage

@allure.feature("forgot password")
@allure.story("Выполнение востановления пароля")
def test_forgot_password(browser):
    link = "http://automationpractice.com/index.php"
    page=MainPage(browser,link)
    page.open()
    page.should_be_button_sign_in()
    page.go_to_sign_in()
    sign_in_page=SignInPage(browser, browser.current_url)
    sign_in_page.should_be_sign_in_url()
    sign_in_page.should_be_button_forgot()
    sign_in_page.go_to_forgot()
    forgot_page=ForgotPage(browser, browser.current_url)
    forgot_page.should_be_forgot_your_password()
    forgot_page.should_be_input_mail()
    forgot_page.input_mail()
    forgot_page.should_be_retrieve_button()
    forgot_page.go_to_retrieve()
    forgot_page.should_be_url_retrieve()
