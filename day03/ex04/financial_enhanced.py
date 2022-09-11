import sys
import urllib3
import certifi
import cProfile
import pstats
from bs4 import BeautifulSoup as bs


def get_data(ticker: str, field: str) -> tuple:
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    http = urllib3.PoolManager(ca_certs=certifi.where())
    page = http.request(method='GET', url=url, headers={'User-Agent': 'DS Piscine'}, redirect=False)
    if page.status != 200:
        raise Exception("Page doesn't exist")
    soup = bs(page.data.decode('utf-8'), 'html.parser')
    lines = soup.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
    for line in lines:
        if line.find('span').text.lower() == field.lower():
            return tuple(val.text for val in line)
    raise Exception(f'Field {field} not found')


def main(av):
    if len(av) == 3:
        try:
            print(get_data(av[1], av[2]))
        except Exception as ex:
            print('Exception:', ex)
    else:
        print('2 arguments are needed!')


if __name__ == '__main__':
    profiling = cProfile.Profile()
    profiling.enable()
    main(sys.argv)
    profiling.disable()

    # filename = 'profiling-http.txt'
    # filename = 'profiling-ncalls.txt'
    filename = 'pstats-cumulative.txt'
    with open(filename, 'w') as stream:
        pstats.Stats(profiling, stream=stream).strip_dirs().sort_stats('cumtime').print_stats(5)
