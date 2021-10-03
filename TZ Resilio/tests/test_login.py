import allure
from lib.main_page import MainPage
from lib.sign_in_page import SignInPage
from lib.profile_page import ProfilePage

@allure.feature("Login user")
@allure.story("Выполнение авторизации пользователя")
def test_sign_in(browser):
    link = "http://automationpractice.com/index.php"
    page=MainPage(browser,link)
    page.open()
    page.should_be_button_sign_in()
    page.go_to_sign_in()
    sign_in_page=SignInPage(browser, browser.current_url)
    sign_in_page.should_be_sign_in_url()
    sign_in_page.should_be_input_mail()
    sign_in_page.input_mail()
    sign_in_page.should_be_input_password()
    sign_in_page.input_password()
    sign_in_page.should_be_sign_in_button()
    sign_in_page.go_to_sign_in()
    account_page=ProfilePage(browser, browser.current_url)
    account_page.should_be_account()