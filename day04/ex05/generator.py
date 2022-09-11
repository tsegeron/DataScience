#!/usr/bin/env python

import sys
import resource


def foo():
    with open(sys.argv[1]) as file:
        for line in file:
            yield line


if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            for line in foo():
                pass
        except Exception as ex:
            print(ex)
    else:
        print('Filename as argument is needed!')
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print(f'Peak Memory Usage = {usage.ru_maxrss / 1024**3:.3f} GB')
    print(f'User Mode Time + System Mode Time = {usage.ru_utime + usage.ru_stime:.2f}s')
