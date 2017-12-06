#!/usr/bin/env python3

banks = [0, 2, 7, 0]
banks = list(map(int, open('day-6-data').readline().strip().split('\t')))

def index_of_max(banks):
    largest = max(banks)
    for i, elem in enumerate(banks):
        if elem == largest:
            return i
    raise Exception('oh no')
assert index_of_max([0, 2, 7, 0]) == 2

def modular_range(start, highest):
    'modular_range(2, 3) -> 2, 3, 0, 1, 2, 3, 0, ...'
    cur = start
    while True:
        cur = cur % highest
        yield cur
        cur += 1
assert [x for _, x in zip(range(5), modular_range(2, 3))] == [2, 0, 1, 2, 0]
assert [x for _, x in zip(range(5), modular_range(4, 3))] == [1, 2, 0, 1, 2]

def redistribute(banks):
    result = list(banks)
    bank_with_most = index_of_max(result)
    tokens_to_distribute = banks[bank_with_most]
    result[bank_with_most] = 0
    for _, x in zip(range(tokens_to_distribute),
                    modular_range(bank_with_most+1, len(result))):
        result[x] += 1
    return result

def applications(func, value):
    while True:
        yield value
        value = func(value)

seen = dict()
for i, state in enumerate(applications(redistribute, banks)):
    print(state)
    slug = '-'.join(map(str,state))
    if slug in seen:
        break
    seen[slug] = i

print(i)
