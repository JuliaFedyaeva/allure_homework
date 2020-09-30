from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/'


class LoginPageLocators():
    LOGIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_FORM_PASSWORD_REPEAT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_FORM_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    SUCCESS_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, 'div.alert.alert-success.fade.in')
    SUCCESS_REGISTRATION_ICON = (By.CSS_SELECTOR, 'i.icon-ok-sign')

    AUTHORIZATION_FORM_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    AUTHORIZATION_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
