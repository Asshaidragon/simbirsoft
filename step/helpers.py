import csv
import datetime

import allure
from allure_commons.types import AttachmentType


def calculate_fibonacci_number_for_current_day() -> int:
    current_day: int = datetime.datetime.now().day
    fibonacci_numbers: list = [0, 1]
    while len(fibonacci_numbers) != current_day + 1:
        fibonacci_numbers.append(fibonacci_numbers[-2] + fibonacci_numbers[-1])
    return fibonacci_numbers.pop()


def attach_file_with_transactions(transactions: list) -> None:
    date_for_csv = []
    for transaction in transactions:
        time, amount, type_transaction = transaction.text.rsplit(maxsplit=2)
        date_time_obj = datetime.datetime.strptime(time, "%b %d, %Y %I:%M:%S %p")
        date_for_csv.append(
            (
                date_time_obj.strftime("%d %B %Y %H:%M:%S"),
                int(amount),
                type_transaction,
            )
        )

    with open("transactions.csv", "wt") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerows(date_for_csv)

    allure.attach.file(
        "./transactions.csv",
        name="transactions.csv",
        attachment_type=AttachmentType.CSV,
    )
