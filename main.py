from src.masks import convert_account_to_mask, convert_number_card_to_mask

card = "1234567890123456"
acc = "12345678901234567890"
print(convert_number_card_to_mask(card))
print(convert_account_to_mask(acc))
