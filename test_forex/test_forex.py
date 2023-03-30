from datetime import date

import pytest
import requests
import json

api_key = '61c1b237d2-e6ccb4d475-rrvc6b'
url = 'https://api.fastforex.io'


# def open_json_currencies(path):
#     with open('test_forex/data/json_currencies.json') as file:
#         return json.load(file)


def open_json_data(path):
    with open(path) as file:
        return json.load(file)


class TestForex:

    para_data = open_json_data('test_forex/data/json_currencies.json')
    data_to_fetch_one = open_json_data('test_forex/data/data.json')['data_fetch_one']
    data_to_convert = open_json_data('test_forex/data/data.json')['data_to_convert']

    def test_all_currencies_names(self):
        endpoint = f"{url}/currencies?api_key={api_key}"
        response = requests.get(endpoint).json()['currencies']
        assert response == self.para_data
        assert len(response) == len(self.para_data)

    @pytest.mark.parametrize('currency1, currency2, exchange_rate, error',  data_to_fetch_one)
    def test_fetch_one(self, currency1, currency2, exchange_rate, error):
        endpoint = f"{url}/fetch-one?from={currency1}&to={currency2}&api_key={api_key}"
        response = requests.get(endpoint).json()
        if error:
            assert response['error'] == error
        else:
            target_currency = list(response['result'].keys())[0]
            response_exchange_rate = float(list(response['result'].values())[0])
            today = str(date.today())
            assert response['base'] == currency1
            assert target_currency == currency2
            assert (exchange_rate[0] <= response_exchange_rate <= exchange_rate[1])
            assert response['updated'].split(' ')[0] == today

    @pytest.mark.parametrize('currency1, currency2, amount, expected_result', data_to_convert)
    def test_convert(self, currency1, currency2, amount, expected_result):
        endpoint = f"{url}/convert?from={currency1}&to={currency2}&amount={amount}&api_key={api_key}"
        response = requests.get(endpoint).json()
        converted = response['result'][currency2]
        assert response['base'] == currency1
        assert response['amount'] == amount
        assert (expected_result[0] <= converted <= expected_result[1])
