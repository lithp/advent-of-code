#!/usr/bin/env python3

from itertools import count, islice
from collections import namedtuple

Coord = namedtuple('Coord', ('x', 'y'))

ring_maxes = dict()
def ring_max(r):
    '''
    1     -> 0
    2-9   -> 1
    10-25 -> 2

    if you're in ring x, your max is ring x-1 + (side_length)*4 + 4
    side_length(ring -> length)
        1 -> 1
        2 -> 3
        3 -> 5
        4 -> 7
        5 -> 9
    '''
    if r == 0:
        return 1
    if r not in ring_maxes:
        ring_maxes[r] = ring_max(r-1) + (r*2 - 1)*4 + 4
    return ring_maxes[r]

print(next(filter(lambda x: x > 347991, map(ring_max, range(10000)))))

def coord(num):
    '''
    1 -> (0, 0)
    9 -> (1, -1)
    25 -> (2, -2)
    '''
    raise NotImplemented

# careful! off-by-one
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

print(list(islice(coords(),0, 347991)))
