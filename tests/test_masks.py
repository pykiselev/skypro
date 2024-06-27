import pytest

from src.masks import convert_account_to_mask, convert_number_card_to_mask


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("", ""),
    ],
)
def test_convert_number_card_to_mask(string, expected_result):
    assert convert_number_card_to_mask(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("12345678901234567890", "**7890"),
        ("", ""),
    ],
)
def test_convert_account_to_mask(string, expected_result):
    assert convert_account_to_mask(string) == expected_result

