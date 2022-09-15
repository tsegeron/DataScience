def my_sort():
    d = {
        'Russia': '25',
        'France': '132',
        'Germany': '132',
        'Spain': '178',
        'Italy': '162',
        'Portugal': '17',
        'Finland': '3',
        'Hungary': '2',
        'The Netherlands': '28',
        'The USA': '610',
        'The United Kingdom': '95',
        'China': '83',
        'Iran': '76',
        'Turkey': '65',
        'Belgium': '34',
        'Canada': '28',
        'Switzerland': '26',
        'Brazil': '25',
        'Austria': '14',
        'Israel': '12'
    }

    [print(item[0]) for item in sorted(d.items(), key=lambda x: (-int(x[1]), x[0]))]


if __name__ == '__main__':
    my_sort()
