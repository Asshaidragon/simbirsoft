from typing import Final

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.AccountPage import AccountPage

CREDIT: Final[str] = "Credit"
DEBIT: Final[str] = "Debit"


def assert_displayed_balance_shows_expected_value(
    driver: WebDriver, amount: int
) -> None:
    assert AccountPage(driver).get_current_balance() == amount, (
        "The current balance does not match the expected one.\n"
        f"Expected: {amount}\nActual: {AccountPage(driver).get_current_balance()}"
    )


def assert_replacement_and_debating_operations_are_present_in_transaction_list(
    transactions: list, amount: int
) -> None:
    test_transactions: list = [
        transaction for transaction in transactions if str(amount) in transaction.text
    ]
    assert (
        len(test_transactions) == 2
    ), "There are more values than expected in the list of text transactions."
    assert (
        f"{amount} {CREDIT}" in test_transactions[0].text
    ), "There is no deposit operation in transactions."
    assert (
        f"{amount} {DEBIT}" in test_transactions[1].text
    ), "There is no withdrawal operation from the account in transactions."
