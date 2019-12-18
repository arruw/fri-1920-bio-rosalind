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
TransitionMatrix = dict2log2(TransitionMatrix)
EmissionMatrix = dict2log2(EmissionMatrix)

# print("Transition Matrix")
# pprint(TransitionMatrix)
# print()
# print("Emissions Matrix")
# pprint(EmissionMatrix)
States.append('-')

# X = 'oo_'
# Sigma = ['o', '_']
# States = ['F', 'L', '-']
# TransitionMatrix = {
#     '-': { '-': .0, 'F': .5, 'L': .5},
#     'F': { '-': .0, 'F': .8, 'L': .2},
#     'L': { '-': .0, 'F': .1, 'L': .9}
# }
# EmissionMatrix = {
#     '-': { 'o': .0, '_': .0 },
#     'F': { 'o': .5, '_': .5 },
#     'L': { 'o': .9, '_': .1 },
# }

# X = 'GGCACTGAA'
# Sigma = ['A', 'C', 'G', 'T']
# States = ['-', 'H', 'L']
# TransitionMatrix = {
#     '-': { 'H': log2(.5), 'L': log2(.5), '-': -inf },
#     'H': { 'H': log2(.5), 'L': log2(.5), '-': -inf },
#     'L': { 'H': log2(.4), 'L': log2(.6), '-': -inf }
# }
# EmissionMatrix = {
#     '-': { 'A': -inf,     'C': -inf,     'G': -inf,     'T': -inf     },
#     'H': { 'A': log2(.2), 'C': log2(.3), 'G': log2(.3), 'T': log2(.2) },
#     'L': { 'A': log2(.3), 'C': log2(.2), 'G': log2(.2), 'T': log2(.3) },
# }

# print("Transition")
# pprint(TransitionMatrix)
# print()
# print("Emission")
# pprint(EmissionMatrix)
# print()

p = {s:(-inf, None) for s in States}
p['-'] = (0, None)
path = list()

for x in X:
    np = dict()
    for to_state in States:
        ts = [p[from_state][0]+TransitionMatrix[from_state][to_state] for from_state in States]
        tsm = max(ts)
        tsmi = ts.index(tsm) 
        
        np[to_state] = (EmissionMatrix[to_state][x] + tsm, States[tsmi])
    path.append(np)
    p = np

# backtrack
result = ''
prev = None
for x in path[::-1]:
    if prev == None:
        curr = max(x.items(), key=lambda y: y[1][0])
        result += curr[0]
        curr = curr[1]
    else:
        curr = x[prev]
        result += prev
    prev = curr[1]

print(result[::-1])

# https://personal.utdallas.edu/~prr105020/biol6385/2018/lecture/Viterbi_handout.pdf