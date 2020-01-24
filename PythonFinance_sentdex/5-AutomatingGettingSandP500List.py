import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, features="lxml")
    # table that contains s&p 500 companies
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []

    print(table)

    # ignore the first row because it's the header row of the table
    for row in table.findAll('tr')[1:]:
        # ticker of the company for that row, 
        # which is what we're interested in
        ticker = row.findAll('td')[0].text.replace('\n','')
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

save_sp500_tickers()
