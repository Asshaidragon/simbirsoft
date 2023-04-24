from selenium.webdriver.chrome.webdriver import WebDriver

from pages.AccountPage import AccountPage
from pages.TransactionPage import TransactionPage


def get_all_transactions(driver: WebDriver) -> list:
    account_page = AccountPage(driver)
    account_page.open_transaction_page()
    transaction_page = TransactionPage(driver)
    return transaction_page.get_all_transactions()
