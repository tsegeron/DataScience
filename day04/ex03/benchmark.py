#!/usr/bin/env python

import timeit
import sys
from functools import reduce


def with_loop(num):
    squares_sum = 0
    for n in range(1, num + 1):
        squares_sum += n**2


def with_reduce(num):
    res = reduce(lambda x, y: x + y**2, range(1, num + 1))


if __name__ == '__main__':
    if len(sys.argv) == 4 and sys.argv[1] != '':
        try:
            print(timeit.timeit(stmt=f'with_{sys.argv[1].replace(" ", "_")}({int(sys.argv[3])})',
                                setup=f'from __main__ import with_{sys.argv[1]}',
                                number=int(sys.argv[2])))
        except Exception:
            print('Incorrect arguments are provided')
    else:
        print('2 arguments are needed!')
