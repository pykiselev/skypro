# import pytest
from src.processing import filter_by_state, sort_by_date


# Попытка решить через параметры
# @pytest.mark.parametrize("transactions, state, expected_result", [
#     (test_transactions, "EXECUTED", result_if_executed),
#     (test_transactions, "CANCELED", result_if_canseled),
# ])
def test_filter_by_state_if_executed(test_transactions, result_if_state_executed):
    assert filter_by_state(test_transactions) == result_if_state_executed


def test_filter_by_state_if_canseled(test_transactions, result_if_state_canseled):
    assert filter_by_state(test_transactions, "CANCELED") == result_if_state_canseled


def test_sort_by_date_if_reverse_false(test_transactions, result_if_reverse_false):
    assert sort_by_date(test_transactions) == result_if_reverse_false


def test_sort_by_date_if_reverse_true(test_transactions, result_if_reverse_true):
    assert sort_by_date(test_transactions, True) == result_if_reverse_true
