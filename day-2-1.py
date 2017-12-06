#!/usr/bin/env python3

lines = open('day-2-data').readlines()

answer = 0
for line in lines:
    line = line.strip()

    row = list(map(int, line.split('\t')))

    big = max(row)
    small = min(row)
    answer += big - small

    print(row, big, small, answer)

print(answer)
