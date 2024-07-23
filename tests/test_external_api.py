from unittest.mock import patch
from src.external_api import currency_conversion
@patch('requests.get')
def test_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37}, 'info': {'timestamp': 1719398417, 'rate': 87.249195}, 'date': '2024-06-26', 'result': 717307.914297}
    test_trans = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    assert currency_conversion(test_trans) == 717307.914297