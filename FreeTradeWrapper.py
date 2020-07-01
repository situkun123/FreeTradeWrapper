import gspread
import pandas as pd
import requests

class FreeTrade(object):
    # class method variables/properties
    def __init__(self, API_key, gsheet_json):
        '''Ensure the json file is in local directory'''
        self.con = gspread.service_account(gsheet_json)
        self.lookup_df = self.all_symbol_info()
        self.API_key = API_key

    def _check_sym_isin(self, x):
        '''Identify if the input is a symbol or isin'''
        if len(x) < 6: # symbol
            return self.find_isin(x)
        else:
            return x

    def all_symbol_info(self):
        data = self.con.open_by_key('14Ep-CmoqWxrMU8HshxthRcdRW8IsXvh3n2-ZHVCzqzQ').get_worksheet(0).get_all_values()
        data_df = pd.DataFrame(data[1:], columns=data[0])
        return data_df

    def find_isin(self, symbol):
        '''Using a symbol to find isin number'''
        df = self.lookup_df
        output = df[df['symbol']== symbol]['isin'].values[0]
        if len(output) == 0:
            return 'No Symbol found!'
        else:
            return output

    def get_symbol(self, isin):
        '''get symbol of a stock'''
        self.url_symbol = f'https://finki.io/callAPI.php?isin={isin}&function=ukSymbol&key={self.API_key}'
        con = requests.get(self.url_symbol)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            symobol = con.content.decode("utf-8").strip('\n')
            return symobol

    def get_bid_price(self, input1):
        '''Get the bid price of a company'''
        input1 = self._check_sym_isin(input1)
        self.url_bid = f'https://finki.io/callAPI.php?isin={input1}&function=ukBid&key={self.API_key}'
        con = requests.get(self.url_bid)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            bid = float(con.content)
            return bid

    def get_ask_price(self, input1):
        '''Get the bid price of a company'''
        input1 = self._check_sym_isin(input1)
        self.url_ask = f'https://finki.io/callAPI.php?isin={input1}&function=ukAsk&key={self.API_key}'
        con = requests.get(self.url_ask)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            bid = float(con.content)
            return bid

    
    def get_currency(self, input1):
        '''Get the currency price of a company'''
        input1 = self._check_sym_isin(input1)
        self.url_currency = f'https://finki.io/callAPI.php?isin={input1}&function=ukCurrency&key={self.API_key}'
        con = requests.get(self.url_currency)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            currency = con.content.decode("utf-8").strip('\n')
            return currency

    
    def get_dividendData(self, input1):
        '''Get dividend data'''
        input1 = self._check_sym_isin(input1)
        self.url_dividend = f'https://finki.io/callAPI.php?isin={input1}&function=dividendData&key={self.API_key}'
        con = requests.get(self.url_dividend)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            dividend = con.content.decode("utf-8").strip('\n')
            return dividend

    
    def get_all_info(self, input1):
        '''Get bid, ask, and currency information'''
        input1 = self._check_sym_isin(input1)
        bid = self.get_bid_price(input1)
        ask = self.get_ask_price(input1)
        currency = self.get_currency(input1)
        symbol = self.get_symbol(input1)

        return {'isin': input1, 'Symbol': symbol, 'bid':bid, 'ask':ask, 'currency':currency}
