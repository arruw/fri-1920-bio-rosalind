#!/usr/bin/python3

from math import log2, inf, ceil
from pprint import pprint
import operator

def read():
    with open('p033/input.txt', 'r') as f:
        return list(map(lambda x: x.replace('\n', ''), f.readlines()))

frags = read()
result = frags.pop()
k = len(result)
while len(frags) > 0:
    for f in frags:
        if result[-k+1:] == f[:k-1]:
            frags.remove(f)
            result += f[-1:]
            continue

# print(result)

# remove cycle
m = result[:ceil(len(result)/2)]
while True:
    if result[-len(m):] == m:
        result = result[:len(result)-len(m)]
        break
    
    m = m[:len(m)-1]

print(result)