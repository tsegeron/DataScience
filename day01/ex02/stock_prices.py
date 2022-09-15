import sys


def stock_prices(av):
    if len(av) != 2:
        return
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    print(STOCKS.get(COMPANIES.get(av[1].capitalize()), 'Unknown company'))


if __name__ == '__main__':
    stock_prices(sys.argv)
