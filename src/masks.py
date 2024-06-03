def convert_number_card_to_mask(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    return card_number[0:4] + " " + card_number[5:7] + "**" + " " + "****" + card_number[-4:]


def convert_account_to_mask(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return "**" + account[-4:]


# def convert_number_card_to_mask(card_number: str): -> str
# """Альтернативная реализация функции"""
#    card_mask = []
#    len_card_number = len(card_number)
#    for i in range(len_card_number):
#        if i < 6 or i > len_card_number-5:
#            card_mask.append(card_number[i])
#        else:
#            card_mask.append("*")
#        if i in [3,7,11]:
#            card_mask.append(" ")
#            return "".join(card_mask)
