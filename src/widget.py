from src.masks import convert_account_to_mask, convert_number_card_to_mask


def masking_card_or_acc(info_card_or_acc: str) -> str:
    """Функция маскировки номера карты/счета"""
    list_info = info_card_or_acc.split(" ")
    len_list = len(list_info)
    if len(list_info[len_list - 1]) == 16:
        list_info[len_list - 1] = convert_number_card_to_mask(list_info[len_list - 1])
    elif len(list_info[len(list_info) - 1]) == 20:
        list_info[len_list - 1] = convert_account_to_mask(list_info[len_list - 1])
    return " ".join(list_info)


def format_date(date: str) -> str:
    """Функция форматирования даты"""
    if date == "":
        return ""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
