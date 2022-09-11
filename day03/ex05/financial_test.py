import requests
from bs4 import BeautifulSoup as bs
import pytest


def get_data(ticker: str, field: str) -> tuple:
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p={ticker}'
    page = requests.get(url=url, headers={'User-Agent': 'DS Piscine'}, allow_redirects=False)
    if page.status_code != 200:
        raise Exception("Page doesn't exist")
    soup = bs(page.text, 'html.parser')
    lines = soup.find_all('div', class_='D(tbr) fi-row Bgc($hoverBgColor):h')
    for line in lines:
        if line.find('span').text.lower() == field.lower():
            return tuple(val.text for val in line)
    raise Exception(f'Field {field} not found')


def main():
    try:
        data = get_data('AAPL', 'Total Revenue')
        print(data)
    except Exception as ex:
        print('Exception:', ex)


if __name__ == '__main__':
    main()


def test_data_type():
    data = get_data('AAPL', 'Total Revenue')
    assert type(data) == tuple


def test_res_content():
    data = get_data('AAPL', 'Total Revenue')
    assert data == ('Total Revenue', '387,542,000', '365,817,000', '274,515,000', '260,174,000', '265,595,000')


def test_exception_ticker():
    with pytest.raises(Exception):
        get_data('asdas', 'Total Revenue')


def test_exception_field():
    with pytest.raises(Exception):
        get_data('AAPL', 'afasfasf')
