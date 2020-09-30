from .pages.data import LoginPageData
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


class TestLoginFromMainPage():
    def test_guest_can_register(self, browser):
        page = MainPage(browser)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser)
        login_page.should_be_register_form()
        login_page.register_new_user(LoginPageData.EMAIL, LoginPageData.PASSWORD)
        login_page.should_be_success_register_message()
        login_page.should_be_success_register_icon()
