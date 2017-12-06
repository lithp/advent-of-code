#!/usr/bin/env python3

result = 0
for passphrase in open('day-4-data').readlines():
    valid = True
    words = dict()
    for word in passphrase.strip().split(' '):
        if word in words:
            valid = False
            break
        words[word] = 1
    if valid:
        result += 1

print(result)
