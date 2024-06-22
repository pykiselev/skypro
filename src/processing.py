from operator import itemgetter


def sort_by_date(transactions: list, is_reverse: bool = False) -> list:
    """Функция сортировки по дате"""
    return sorted(transactions, key=itemgetter("date"), reverse=is_reverse)


def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Функция фильтрации по state"""
    return [trans for trans in transactions if trans["state"] == state]
