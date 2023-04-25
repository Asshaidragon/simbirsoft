import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from pages.AccountPage import AccountPage
from pages.LoginPage import LoginPage
from pages.TransactionPage import TransactionPage
from step.assertions import (
    assert_replacement_and_debating_operations_are_present_in_transaction_list,
    assert_displayed_balance_shows_expected_value,
)
from step.helpers import (
    calculate_fibonacci_number_for_current_day,
    attach_file_with_transactions,
)


def test_replenishment_and_debiting_of_account(driver: WebDriver):
    with allure.step(
        'Step 1: authorization in the account by the user "Harry Potter".'
    ):
        LoginPage(driver).log_in_as_user("Harry Potter")

    with allure.step("Step 2: calculating the Fibonacci number for the current day."):
        fibonacci_number: int = calculate_fibonacci_number_for_current_day()

    with allure.step(
        "Step 3: replenishment of the account for an amount equal to the Fibonacci number."
    ):
        AccountPage(driver).top_up_user_deposit(fibonacci_number)

    with allure.step("Step 4: check that the balance has been topped up."):
        assert_displayed_balance_shows_expected_value(driver, fibonacci_number)

    with allure.step("Step 5: debiting an amount equal to the fibonacci number."):
        AccountPage(driver).make_debit_from_account(fibonacci_number)

    with allure.step("Step 6: check that the balance is 0."):
        assert_displayed_balance_shows_expected_value(driver, 0)

    with allure.step("Step 7: open transaction page."):
        AccountPage(driver).open_transaction_page()

    with allure.step("Step 8: getting all transactions for the account."):
        transactions: list = TransactionPage(driver).get_all_transactions()

    with allure.step(
        "Step 9: checking for transactions with replenishment and debiting."
    ):
        assert_replacement_and_debating_operations_are_present_in_transaction_list(
            transactions, fibonacci_number
        )

    with allure.step("Step 10: attach a file with transactions."):
        attach_file_with_transactions(transactions)
