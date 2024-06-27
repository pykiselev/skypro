from typing import Dict, Generator, List, Union


def filter_by_currency(trans: Union [List[Dict], Generator], currency: str) -> Generator:
    """Генератор фильтра по заданной валюте"""
    return (tran for tran in trans if tran["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(trans: List[Dict]) -> Generator:
    """Функция-генератор описания каждой операции"""
    return (tran["description"] for tran in trans)


def card_number_generator(start: int, end: int) -> Generator:
    """Генератор номеров банковских карт"""
    for num in range(start, end):
        str_num = str(num)
        len_num = len(str_num)
        str_null = "0" * (16 - len_num)
        card = f"{str_null}{str_num}"
        yield f"{card[0:4]} {card[4:8]} {card[8:12]} {card[12:]}"