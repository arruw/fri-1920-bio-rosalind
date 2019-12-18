#!/usr/bin/python3

from math import log2, inf
from pprint import pprint
import operator
import regex as re

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
Y = input()
input()
States = input().split()

TransitionMatrix = dict()
for S in States:
    TransitionMatrix[S] = {s: 1/len(States) for s in States}
    TransitionMatrix[S]['-'] = 0
TransitionMatrix['-'] = {s: 1/len(States) for s in States}
TransitionMatrix['-']['-'] = 0

EmissionMatrix = dict()
for S in States:
    EmissionMatrix[S] = {s: 1/len(Sigma) for s in Sigma}
EmissionMatrix['-'] = {s:0 for s in Sigma}

# Transform probabilities to log2 scale
TransitionMatrix = dict2log2(TransitionMatrix)
EmissionMatrix = dict2log2(EmissionMatrix)
States.append('-')

# do magic
mpp = Y
for l in States:
    for k in States:
        if l == '-' or k == '-':
            a = pow(2, TransitionMatrix[k][l])      
        elif mpp[:-1].count(k) == 0:
            a = 1/(len(States)-1)
        else:
            a = len(list(filter(lambda x: x == (k, l), zip(mpp, mpp[1:])))) / mpp[:-1].count(k)
        TransitionMatrix[k][l] = a

    for b in Sigma:
        if l == '-':
            e = pow(2, EmissionMatrix[l][b])
        elif mpp.count(l) == 0:
            e = 1/(len(States)-1)
        else:
            e = len(list(filter(lambda x: x == (l, b), zip(mpp, X)))) / mpp.count(l)
        EmissionMatrix[l][b] = e
    
def cf(v):
    ret = f'{v:.3f}'.rstrip('0')
    if ret.endswith('.'): ret += '0'
    return ret

#print
print('', end='\t')
for s in States:
    if s == '-': continue
    print(s, end='\t')
print()
for from_s in States:
    if from_s == '-': continue
    print(from_s, end='\t')
    for to_s in States:
        if to_s == '-': continue
        print(f'{cf(TransitionMatrix[from_s][to_s])}', end='\t')
    print()
print('--------')
print('', end='\t')
for x in Sigma:
    print(x, end='\t')
print()
for s in States:
    if s == '-': continue
    print(s, end='\t')
    for x in Sigma:
        print(f'{cf(EmissionMatrix[s][x])}', end='\t')
    print()

