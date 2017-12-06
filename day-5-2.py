#!/usr/bin/env python3

data = open('day-5-data').readlines()

lines = dict()
for i, line in enumerate(data):
    lines[i] = int(line.strip())

pointer = 0
steps = 0

while pointer < len(lines) and pointer >= 0:
    offset = lines[pointer]
    if lines[pointer] >= 3:
        lines[pointer] -= 1
    else:
        lines[pointer] += 1
    pointer += offset
    steps += 1

print(steps)
