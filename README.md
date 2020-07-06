# FreeTradeWrapper
A wrapper for finKi API use for requesting data points for stocks symbol in Free Trade App

## Finki API Key
In order to to obtain API key, you will need to go on https://finki.io/finkiAPI.html to request for API key.

## Google sheet API and Json authentication file 
Please refer to offical documentation: https://developers.google.com/sheets/api/quickstart/python

You can also refer to this awsome article on medium: https://towardsdatascience.com/accessing-google-spreadsheet-data-using-python-90a5bc214fd2

## Free Trade stocks & shares meta infomation
These information can be found in the following google sheet:
https://docs.google.com/spreadsheets/d/14Ep-CmoqWxrMU8HshxthRcdRW8IsXvh3n2-ZHVCzqzQ/edit#gid=1855920257

## Basic Usage
```python
import sys
sys.path.append('your_directory_of_freetrade_class')
from FreeTrade import FreeTrade

sess = FreeTrade(your_api_key) # initialize the session with your finKi API key

sess.get_bid_price('GOOGL') # get bid price of Alphabet by using the trading symbol for it
sess.get_bid_price('US02079K3059') # get bid price of Alphabet by using isin reference number
```
