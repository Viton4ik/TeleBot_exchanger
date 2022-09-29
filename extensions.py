
# import time
# from datetime import datetime
# import requests
import json
from config import *


class ConvetionExcepton(Exception):
    pass

class CurrencyInfo:
    @staticmethod
    ### detailed list of currencies from the file - currency_list.txt
    def get_currency_list():
        detailed_list = {}
        with open('currency_list.txt', 'r') as file:
            for i, line in enumerate(file):
                if i >= 1: # cross out the date info (from the 2d line)
                    inner = eval(line[5:(len(line) - 1)]) #info from inner dictionary
                    detailed_list[inner['id']] = inner['currencyName']
        return detailed_list

    @staticmethod
    ### detailed list of crypto currencies from the file
    def get_crypto_currency_list():
        detailed_list = {}
        with open('crypro_currency_list.txt', 'r') as file:
            for i, line in enumerate(file):
                if i >= 1: # cross out the date info (from the 2d line)
                    ticker, info_ = line.split(':') # split line with a ":"
                    info = info_.split('\n') # delete a 'spacebar'
                    detailed_list[ticker] = info[0]
        return detailed_list

currency_list = CurrencyInfo.get_currency_list() # create a list
crypto_currency_list = CurrencyInfo.get_crypto_currency_list() # create a list

class Converter:
    @staticmethod
    def converter(quote: str, base: str, amount: str):

        if quote in currency_list.keys() or quote in crypto_currency_list.keys():
            quote_ticker = quote
        else:
            raise ConvetionExcepton(f"The value '{quote}' has not been accepted!")

        if base in currency_list.keys() or base in crypto_currency_list.keys():
            base_ticker = base
        else:
            raise ConvetionExcepton(f"The value '{base}' 'has not been accepted!")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvetionExcepton(f"The value '{amount}' has not been accepted!")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}').content
        total_base = json.loads(r)

        return total_base

class Counter:
    @staticmethod
    def count(key): # counter for each function
        converted_cash = json.loads(red.get('cash'))
        converted_cash[key] += 1
        red.set('cash', json.dumps(converted_cash))

