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


if __name__ == '__main__':
    res1 = timeit.timeit(stmt='with_loop()', setup='from __main__ import with_loop', number=90000000)
    res2 = timeit.timeit(stmt='with_list_compr()', setup='from __main__ import with_list_compr', number=90000000)
    print("It's better to use a list comprehension" if res1 > res2 else
          "It's better to use a loop", f'{res2} vs {res1}', sep='\n')
