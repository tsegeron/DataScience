import sys


def ticker_symbols(companies, av):
    for key, val in companies.items():
        if av == val:
            return f'{val} is a ticker symbol for {key}'


def stock_prices(companies, stocks, av):
    if av in companies:
        return f'{av} stock price is {stocks.get(companies.get(av))}'


def not_found(av):
    return av + ' is an unknown company or an unknown ticker symbol'


def all_in(avs):
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
    av = [word.strip() for word in avs.split(',')]
    if '' in av:
        print()
        return

    funcs = ['ticker_symbols(COMPANIES, av[i].upper())',
             'stock_prices(COMPANIES, STOCKS, av[i].title())',
             'not_found(av[i])']

    for i in range(len(av)):
        for func in funcs:
            ret = eval(func)
            if ret:
                print(ret)
                break


if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_in(sys.argv[1])
