#!/usr/bin/env python3

numbers = open('day-1-data').readline().strip()

def halfway(index):
    return (index + (len(numbers) // 2)) % len(numbers)

answer = 0
for i, digit in enumerate(numbers):
    digit = int(digit)
    around = int(numbers[halfway(i)])
    if digit is around:
        answer += digit

print(answer)
