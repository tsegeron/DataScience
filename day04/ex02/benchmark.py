#!/usr/bin/env python

import timeit
import sys


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


def with_list_comprehension():
    res = [elem for elem in get_emails() if 'gmail' in elem]


def with_map():
    emails = get_emails()
    res = map(lambda x: x if 'gmail' in x else None, emails)
    # res = list(map(lambda x: x if 'gmail' in x else None, emails))


def with_filter():
    emails = get_emails()
    res = filter(lambda x: 'gmail' in x, emails)
    # res = list(filter(lambda x: 'gmail' in x, emails))


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] != '':
        try:
            print(timeit.timeit(stmt=f'with_{sys.argv[1].replace(" ", "_")}()',
                                setup=f'from __main__ import with_{sys.argv[1].replace(" ", "_")}',
                                number=int(sys.argv[2])))
        except Exception:
            print('Incorrect arguments are provided')
    else:
        print('2 arguments are needed!')
