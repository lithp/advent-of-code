#!/usr/bin/env python3

lines = open('day-2-data').readlines()

def which_divides(target, rest):
    for num in rest:
        if max(num, target) % min(num, target) == 0:
            return max(num, target) / min(num, target)
    return 0

answer = 0
for line in lines:
    line = line.strip()

    row = list(map(int, line.split('\t')))

    for idx, num in enumerate(row):
        left = row[:idx]
        right = row[idx+1:]

        answer += which_divides(num, left)
        answer += which_divides(num, right)

print(answer // 2)  # every pair is counted twice
