#!/usr/bin/env python3

from itertools import count, islice
from collections import namedtuple, defaultdict

Coord = namedtuple('Coord', ('x', 'y'))
full = defaultdict(int)

def coords():
    cur = Coord(0, 0)
    direction = None
    for i in count():
        yield (i+1), cur

        if cur.x >= 0 and cur.x == -cur.y:
            # bottom-right corner, ready to start another ring!
            cur = Coord(cur.x + 1, cur.y)
            direction = 'up'
            continue

        if cur.x > 0 and cur.x == cur.y:
            # top-right corner, turn left!
            cur = Coord(cur.x - 1, cur.y)
            direction = 'left'
            continue

        if cur.x < 0 and -cur.x == cur.y:
            # top-left corner, turn down!
            cur = Coord(cur.x, cur.y - 1)
            direction = 'down'
            continue

        if cur.x < 0 and -cur.x == -cur.y:
            # bottom-left corner, turn right!
            cur = Coord(cur.x + 1, cur.y)
            direction = 'right'
            continue

        if direction == 'up':
            cur = Coord(cur.x, cur.y + 1)
        elif direction == 'left':
            cur = Coord(cur.x - 1, cur.y)
        elif direction == 'down':
            cur = Coord(cur.x, cur.y-1)
        elif direction == 'right':
            cur = Coord(cur.x + 1, cur.y)
        else:
            raise ValueError('%s %s' % (cur, direction))

def collect(board, coord):
    result = 0
    for (x, y) in [(-1, 1), (0, 1), (1, 1),
                   (-1, 0),         (1, 0),
                   (-1, -1),(0, -1),(1, -1)]:
        result += board[(coord.x + x, coord.y + y)]
    return result

for i, coord in coords():
    if i == 1:
        full[coord] = 1
        continue
    value = collect(full, coord)
    if value > 347991:
        print(value)
        break
    full[coord] = value
