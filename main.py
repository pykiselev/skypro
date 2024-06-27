from src.masks import convert_account_to_mask, convert_number_card_to_mask
from src.processing import filter_by_state, sort_by_date
from src.widget import format_date, masking_card_or_acc

card = "1234567890123456"
acc = "12345678901234567890"
info_card = "Visa Classic 6831982476737658"
info_acc = "Счет 35383033474447895560"
test_date = "2018-07-11T02:26:18.671407"
print(convert_number_card_to_mask(card))
print(convert_account_to_mask(acc))
print(masking_card_or_acc(info_card))
print(masking_card_or_acc(info_acc))
print(format_date(test_date))
test_list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(test_list_dict, "CANCELED"))
print(sort_by_date(test_list_dict))
