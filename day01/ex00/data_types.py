def data_types():
    data = [1, '1', 1., True, [1, ], {1: '1'}, (1, ), {1}]
    print('[' + ', '.join(type(x).__name__ for x in data) + ']')


if __name__ == '__main__':
    data_types()
