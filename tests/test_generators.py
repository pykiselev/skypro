import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_transactions_info):
    temp_list = []
    test_usd_transactions = filter_by_currency(test_transactions_info, "USD")
    for _ in range(2):
        temp_list.append(next(test_usd_transactions)["id"])
    assert temp_list == [939719570, 142264268]


def test_transaction_descriptions(test_transactions_info):
    temp_list = []
    test_descriptions = transaction_descriptions(test_transactions_info)
    for _ in range(5):
        temp_list.append(next(test_descriptions))
    assert temp_list == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


@pytest.mark.parametrize(
    "start, end, expected_result",
    [(1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"])],
)
def test_card_number_generator(start, end, expected_result):
    temp_list = []
    for card_number in card_number_generator(start, end):
        temp_list.append(card_number)
    assert temp_list == expected_result