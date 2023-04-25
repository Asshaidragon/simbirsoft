from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from framework.BasePage import BasePage


class TransactionPageLocators:
    LIST_WITH_TRANSACTION = (
        By.XPATH,
        "/html/body/div/div/div[2]/div/div[2]/table/tbody/tr",
    )


class TransactionPage(BasePage):
    def get_all_transactions(self) -> list:
        for _ in range(5):
            try:
                return self.get_elements(TransactionPageLocators.LIST_WITH_TRANSACTION)
            except TimeoutException:
                self.driver.refresh()

        raise AssertionError("The transaction list is empty")
