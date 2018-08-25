import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://www.finviz.com/'
URL_SCREENER = URL_BASE + 'screener.ashx'

# filters is a list of url key strings to be concatenated into the final search
# url
def query_stocks(filters):
    next_stock_index = 1
    total_stocks = 0

    # extract only ticker, name, and link
    tickers = []
    names = []
    links = []

    # loop through all pages of stocks
    while True:
        # construct the url
        if len(filters) > 0:
            url_options = '?&f=' + ','.join(filters) + '&r=' + str(next_stock_index)
            url_filter = URL_SCREENER + url_options
        else:
            url_filter = URL_SCREENER

        page = requests.get(url_filter)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        # parse total stocks listed
        e_total = soup.find_all('td', {'class': 'count-text'})[0]
        total_stocks = int(e_total.get_text().split(' ')[1])

        # break if there are no more listings
        if next_stock_index > total_stocks:
            break

        queried_stock_rows = soup.find_all('tr', {'class': 
            ['table-dark-row-cp', 'table-light-row-cp']})
        queried_stock_items = [stock.find_children('td', recursive=False)[1:3]
                for stock in queried_stock_rows]
        
        for stock in queried_stock_items:
            a_ticker = stock[0].find_children('a')[0]
            a_name = stock[1].find_children('a')[0]
            tickers.append(a_ticker.get_text())
            names.append(a_name.get_text())
            links.append(URL_BASE + a_ticker['href'])
        
        next_stock_index += len(queried_stock_items)

    # create pandas df from html elements
    df_queried_stocks = pd.DataFrame({
        'ticker': tickers,
        'name': names,
        'link': links})

    return df_queried_stocks

def get_url_marketwatch(url_finviz):
    page = requests.get(url_finviz)
    soup = BeautifulSoup(page.content, 'html.parser')

    url_statement = soup.find('a', string='statements')['href']
    
    
