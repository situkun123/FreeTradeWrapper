import requests

class FreeTrade(object):

    def __init__(self, API_key):
        '''Ensure the json file is in local directory'''
        self.API_key = API_key

        def get_symbol(self, isin):
        '''get symbol of a stock'''
        self.url_symbol = f'https://finki.io/callAPI.php?isin={isin}&function=ukSymbol&key={self.API_key}'
        con = requests.get(self.url_symbol)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            symobol = con.content.decode("utf-8").strip('\n')
            return symobol

    def get_bid_price(self, isin):
        '''Get the bid price of a company'''
        self.url_bid = f'https://finki.io/callAPI.php?isin={isin}&function=ukBid&key={self.API_key}'
        con = requests.get(self.url_bid)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            bid = float(con.content)
            return bid

    def get_ask_price(self, isin):
        '''Get the bid price of a company'''
        self.url_ask = f'https://finki.io/callAPI.php?isin={isin}&function=ukAsk&key={self.API_key}'
        con = requests.get(self.url_ask)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            bid = float(con.content)
            return bid

    
    def get_currency(self, isin):
        '''Get the currency price of a company'''
        self.url_currency = f'https://finki.io/callAPI.php?isin={isin}&function=ukCurrency&key={self.API_key}'
        con = requests.get(self.url_currency)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            currency = con.content.decode("utf-8").strip('\n')
            return currency

    
    def get_dividendData(self, isin):
        '''Get dividend data'''
        self.url_dividend = f'https://finki.io/callAPI.php?isin={isin}&function=dividendData&key={self.API_key}'
        con = requests.get(self.url_dividend)
        if con.status_code != 200:
            return 'Connection failed!'
        else:
            dividend = con.content.decode("utf-8").strip('\n')
            return dividend


    def get_all_info(self, isin):
        '''Get bid, ask, and currency information'''
        bid = self.get_bid_price(isin)
        ask = self.get_ask_price(isin)
        currency = self.get_currency(isin)
        symbol = self.get_symbol(isin)

        return {'isin': isin, 'Symbol': symbol, 'bid':bid, 'ask':ask, 'currency':currency}
