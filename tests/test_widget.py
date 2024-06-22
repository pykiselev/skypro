import pytest

from src.widget import format_date, masking_card_or_acc


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_masking_card_or_acc(string, expected_result):
    assert masking_card_or_acc(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_format_date(string, expected_result):
    assert format_date(string) == expected_result