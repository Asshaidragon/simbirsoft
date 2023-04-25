from typing import Final

from selenium.webdriver.common.by import By

from framework.BasePage import BasePage

LOGIN_PAGE_URL: Final[
    str
] = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"


class LoginPageLocators:
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, '//*[@ng-click="customer()"]')
    USER_NAMES_SELECTORS = (By.XPATH, '//*[@id="userSelect"]')
    LIST_OF_USER_NAMES = (By.XPATH, '//*[@id="userSelect"]/option')
    LOGIN_BUTTON = (By.XPATH, '//*[@name="myForm"]/button')


class LoginPage(BasePage):
    def log_in_as_user(self, name: str) -> None:
        self.go_to_url(LOGIN_PAGE_URL)
        self.click(LoginPageLocators.CUSTOMER_LOGIN_BUTTON)
        self.click(LoginPageLocators.USER_NAMES_SELECTORS)
        user_names: list = self.get_elements(LoginPageLocators.LIST_OF_USER_NAMES)
        user_names.pop(0)
        [user.click() for user in user_names if user.text == name]
        self.click(LoginPageLocators.LOGIN_BUTTON)
