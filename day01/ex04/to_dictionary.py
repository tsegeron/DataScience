def var_to_dict():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]

    _dict = dict()
    for val, key in list_of_tuples:
        _dict[key] = val if not _dict.get(key) else _dict.get(key) + f', {val}'

    [print(f"'{key}' : '{v}'") for key, val in _dict.items() for v in val.split(', ')]


if __name__ == '__main__':
    var_to_dict()
