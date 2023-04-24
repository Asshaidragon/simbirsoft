from selenium.webdriver.common.by import By

from framework.BasePage import BasePage


class AccountPageLocators:
    TRANSACTION_BUTTON = (By.XPATH, '//*[@ng-click="transactions()"]')
    DEPOSIT_BUTTON = (By.XPATH, '//*[@ng-click="deposit()"]')
    WITHDRAW_BUTTON = (By.XPATH, '//*[@ng-click="withdrawl()"]')
    DEPOSIT_AMOUNT_INPUT = (By.XPATH, '//*[@ng-submit="deposit()"]/div/input')
    CONFIRM_TOP_UP_BUTTON = (By.XPATH, '//*[@ng-submit="deposit()"]/button')
    CURRENT_BALANCE_TEXT = (By.XPATH, '//*[@ng-hide="noAccount"]/strong[2]')
    WITHDRAW_AMOUNT_INPUT = (By.XPATH, '//*[@ng-submit="withdrawl()"]/div/input')
    DEBIT_CONFIRMATION_BUTTON = (By.XPATH, '//*[@ng-submit="withdrawl()"]/button')


class AccountPage(BasePage):
    def top_up_user_deposit(self, amount: int) -> None:
        self.click(AccountPageLocators.DEPOSIT_BUTTON)
        self.send_keys(AccountPageLocators.DEPOSIT_AMOUNT_INPUT, str(amount))
        self.click(AccountPageLocators.CONFIRM_TOP_UP_BUTTON)

    def get_current_balance(self) -> int:
        return int(self.get_element(AccountPageLocators.CURRENT_BALANCE_TEXT).text)

    def make_debit_from_account(self, amount: int) -> None:
        self.click(AccountPageLocators.WITHDRAW_BUTTON)
        self.send_keys(AccountPageLocators.WITHDRAW_AMOUNT_INPUT, str(amount))
        self.click(AccountPageLocators.DEBIT_CONFIRMATION_BUTTON)

    def open_transaction_page(self) -> None:
        self.click(AccountPageLocators.TRANSACTION_BUTTON)
