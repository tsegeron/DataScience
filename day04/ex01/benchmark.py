#!/usr/bin/env python

import timeit


def get_emails():
    # return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
    return ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
            'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
            'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
            'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com',
            'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    # to not waste the time on list enlarging


def with_loop():
    res = []
    for elem in get_emails():
        if 'gmail' in elem:
            res.append(elem)


def with_list_compr():
    res = [elem for elem in get_emails() if 'gmail' in elem]


def with_map():
    emails = get_emails()
    res = map(lambda x: x if 'gmail' in x else None, emails)
    # res = list(map(lambda x: x if 'gmail' in x else None, emails))
    # res = filter(lambda x: x if 'gmail' in x else None, emails)


if __name__ == '__main__':
    res = {timeit.timeit(stmt='with_loop()', setup='from __main__ import with_loop', number=90000000): 'loop',
           timeit.timeit(stmt='with_list_compr()', setup='from __main__ import with_list_compr', number=90000000): 'list comprehension',
           timeit.timeit(stmt='with_map()', setup='from __main__ import with_map', number=90000000): 'map'}
    keys = sorted(res, key=lambda x: x)
    print(f"It's better to use a {res[keys[0]]}",
          f'{keys[0]} vs {keys[1]} vs {keys[2]}', sep='\n')
    # It's better to use a map
    # 28.345206789002987 vs 124.58580235802219 vs 153.02838982301182
