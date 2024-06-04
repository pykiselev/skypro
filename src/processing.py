from operator import itemgetter

def sort_by_date(list_dict: list, is_reverse: bool = False) -> list:
    return sorted(list_dict, key = itemgetter("date"), reverse=is_reverse)
    #return sorted(list_dict, key=lambda x: datetime.datetime.strptime(x["date"],"%Y-%m-%d"), reverse=is_reverse)

def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    return [d for d in list_dict if d["state"] == state]