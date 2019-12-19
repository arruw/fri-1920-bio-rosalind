#!/usr/bin/python3

from math import log2, inf
from pprint import pprint
import operator

def dict2log2(d):
    nd1 = dict()
    for k1,v1 in d.items():
        nd2 = dict()
        for k2,v2 in v1.items():
            if v2 == 0:
                nd2[k2] = -inf
            else:
                nd2[k2] = log2(v2)
        nd1[k1] = nd2
    return nd1

X = input()
input()
Sigma = input().split()
input()
States = input().split()
input()
input()
TransitionMatrix = dict()
for S in States:
    TransitionMatrix[S] = dict(zip(States, list(map(float, input().split()[1:]))))
    TransitionMatrix[S]['-'] = 0
TransitionMatrix['-'] = {s: 1/len(States) for s in States}
TransitionMatrix['-']['-'] = 0

input()
input()
EmissionMatrix = dict()
for S in States:
    EmissionMatrix[S] = dict(zip(Sigma, list(map(float, input().split()[1:]))))
EmissionMatrix['-'] = {s:0 for s in Sigma}

# Transform probabilities to log2 scale
# TransitionMatrix = dict2log2(TransitionMatrix)
# EmissionMatrix = dict2log2(EmissionMatrix)

# print("Transition Matrix")
# pprint(TransitionMatrix)
# print()
# print("Emissions Matrix")
# pprint(EmissionMatrix)
States.append('-')

prev = {s:0.0 for s in States}
prev['-'] = 1.0
for i in X:
    curr = dict()
    for l in States:
        curr[l] = EmissionMatrix[l][i] * sum([prev[k]*TransitionMatrix[k][l] for k in States])
    prev = curr

print(sum([v for _,v in prev.items()]))