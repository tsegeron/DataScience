import sys


def ticker_symbols(av):
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

    for key, val in COMPANIES.items():
        if av[1].lower() == val.lower():
            return val + ' ' + str(STOCKS.get(val.upper()))
    return 'Unknown ticker'


if __name__ == '__main__':
    print(ticker_symbols(sys.argv))
