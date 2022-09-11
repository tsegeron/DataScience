import requests
import time
import sys
from bs4 import BeautifulSoup as bs


def get_data(ticker: str, field: str) -> tuple:
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    page = requests.get(url=url, headers={'User-Agent': 'DS Piscine'}, allow_redirects=False)
    if page.status_code != 200:
        raise Exception("Page doesn't exist")
    # res = []
    soup = bs(page.text, 'html.parser')
    lines = soup.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
    for line in lines:
        if line.find('span').text.lower() == field.lower():
            return tuple(val.text for val in line)
    #     if field.lower() in line.find('span').text.lower():   # in case if we want to get all fields including 'field'
    #         res.append(tuple(val.text for val in line))
    # if len(res) != 0:
    #     return tuple(res)
    raise Exception(f'Field {field} not found')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        try:
            print(get_data(sys.argv[1], sys.argv[2]))
        except Exception as ex:
            print('Exception:', ex)
        time.sleep(5)
    else:
        print('2 arguments are needed!')
