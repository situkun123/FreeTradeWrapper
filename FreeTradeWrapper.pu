import requests

class FreeTrade(object):
    # class method variables/properties

    def __init__(self, API_key):
        '''Ensure the json file is in local directory'''
        self.API_key = API_key

    def get_bid_price(self, isin):
        '''Get the bid price of a company'''
        url_bid = f'https://finki.io/callAPI.php?isin={isin}&function=ukBid&key={self.API_key}'
        bid = float(requests.get(url_bid).content)
        return bid

    
    def get_ask_price(self, isin):
        '''Get the bid price of a company'''
        url_ask = f'https://finki.io/callAPI.php?isin={isin}&function=ukAsk&key={self.API_key}'
        bid = float(requests.get(url_ask).content)
        return bid

    
    def get_currency(self, isin):
        '''Get the currency price of a company'''
        url_currency = f'https://finki.io/callAPI.php?isin={isin}&function=ukCurrency&key={self.API_key}'
        currency = requests.get(url_currency).content.decode("utf-8").strip('\n')
        return currency

    
    def get_dividendData(self, isin):
        '''Get dividend data'''
        url_dividend = f'https://finki.io/callAPI.php?isin={isin}&function=dividendData&key={self.API_key}'
        dividend = requests.get(url_dividend).content.decode("utf-8").strip('\n')
        return dividend

    
    def get_all_info(self, isin):
        bid = self.get_bid_price(isin)
        ask = self.get_ask_price(isin)
        currency = self.get_currency(isin)
        return {'bid':bid, 'ask':ask, 'currency':currency}
