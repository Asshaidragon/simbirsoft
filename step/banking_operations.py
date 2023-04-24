from selenium.webdriver.chrome.webdriver import WebDriver

from pages.AccountPage import AccountPage


def top_up_user_deposit(driver: WebDriver, amount: int) -> None:
    account_page = AccountPage(driver)
    account_page.top_up_user_deposit(amount)


def make_debit_from_account(driver: WebDriver, amount: int) -> None:
    account_page = AccountPage(driver)
    account_page.make_debit_from_account(amount)


def get_balance(driver: WebDriver) -> int:
    account_page = AccountPage(driver)
    return account_page.get_current_balance()
