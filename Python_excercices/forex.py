import requests
from pprint import PrettyPrinter
from datetime import date
import json


class Currencies:

    api_key = '61c1b237d2-e6ccb4d475-rrvc6b'
    url = 'https://api.fastforex.io'
    printer = PrettyPrinter()

    def all_currencies(self):
        endpoint = f"{self.url}/currencies?api_key={self.api_key}"
        response = requests.get(endpoint).json()['currencies']
        return response

    def save_json_all_currencies(self):
        all_currencies = self.all_currencies()
        data = json.dumps(all_currencies, indent=2)
        with open('../test_forex/data/json_currencies.json', 'w+') as file:
            file.write(data)

    def get_all_currency_rate(self, currency='USD'):
        endpoint = f'{self.url}/fetch-all?from={currency}&api_key={self.api_key}'
        response = requests.get(endpoint).json()
        return response

    def time_series_last_14_days(self, currency1, currency2):
        today = date.today()
        two_weeks_ago = today.replace(day=today.day - 14)
        endpoint = f"{self.url}/time-series?from={currency1}&to={currency2}&start={two_weeks_ago}&end={today}&interval=P1D&api_key={self.api_key}"
        response = requests.get(endpoint).json()['results'][currency2]
        return response

    def display_table(self, currency1, currency2):
        response = self.time_series_last_14_days(currency1, currency2)
        return self.printer.pprint(response)

    def exchange_rate(self, currency1, currency2):
        endpoint = f"{self.url}/fetch-multi?from={currency1}&to={currency2}&api_key={self.api_key}"
        response = requests.get(endpoint).json()
        return response

    def lowest_exchange_rate_14_days(self, currency1, currency2):
        min_value = min(self.time_series_last_14_days(currency1, currency2).values())
        return min_value

    def display_exchange_rate(self, currency1, currency2):
        exchange_rate = self.exchange_rate(currency1, currency2)['results'][currency2]
        print(f'Exchange rate from {currency1} to {currency2} is {exchange_rate}.')

    def convert_currencies(self, currency1, currency2, amount):
        rate = self.exchange_rate(currency1, currency2)['results'][currency2]
        return rate * int(amount)

    def main(self):
        currencies = self.all_currencies()
        print('Welcome to currency converter')

        while True:
            print('>> Chose between List, Convert, Rate, Rate to all <<')
            command = input('If want to quit enter q ').lower()
            if command == 'q':
                break
            elif command == 'list':
                self.printer.pprint(currencies)
            elif command == 'rate':
                currency1 = input('From currency, enter 3-letter symbol: ').upper()
                currency2 = input('To currency, enter 3-letter symbol: ').upper()
                self.display_exchange_rate(currency1, currency2)
            elif command == 'rate to all':
                currency = input('Enter 3-letter symbol: ').upper()
                get_all = self.get_all_currency_rate(currency=currency)['results']
                self.printer.pprint(get_all)
            elif command == 'convert':
                currency1 = input('From currency, enter 3-letter symbol: ').upper()
                currency2 = input('To currency, enter 3-letter symbol: ').upper()
                amount = input('What amount do You want to exchange: ')
                print(f'For {amount} of {currency1} You will get '
                      f'{self.convert_currencies(currency1, currency2, amount)} of {currency2}')


# Currencies().main()
Currencies().save_json_all_currencies()