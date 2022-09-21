#!/usr/bin/env python

import timeit
import random
from collections import Counter


def get_nums():
    return [random.randint(0, 100) for _ in range(1000000)]


def dict_from_list(list_of_values: list[int]) -> dict:
    return {key: list_of_values.count(key) for key in range(0, 101)}


def top_10(list_of_values: list[int]) -> dict:
    return dict(sorted(dict_from_list(list_of_values).items(), key=lambda x: -x[1])[:10])


def counter_dict_from_list(list_of_values: list[int]):
    return dict(Counter(list_of_values))


def counter_top_10(list_of_values: list[int]) -> dict:
    return dict(Counter(list_of_values).most_common(10))


if __name__ == '__main__':
    vals = get_nums()

    # print(dict_from_list(vals))
    # print(counter_dict_from_list(vals))
    # print(top_10(vals))
    # print(counter_top_10(vals))

    print('My function:', timeit.timeit(stmt='dict_from_list(vals)',
                                        setup='from __main__ import dict_from_list, vals', number=1))
    print('Counter:', timeit.timeit(stmt='counter_dict_from_list(vals)',
                                    setup='from __main__ import counter_dict_from_list, vals', number=1))

    print("My function's top:", timeit.timeit(stmt='top_10(vals)',
                                              setup='from __main__ import top_10, vals', number=1))
    print("Counter's top:", timeit.timeit(stmt='counter_top_10(vals)',
                                          setup='from __main__ import counter_top_10, vals', number=1))
