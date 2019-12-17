#!/usr/bin/python3

from math import log2, inf
from pprint import pprint

def log2float(s):
    return log2(float(s))

X = input()
input()
Sigma = input().split()
input()
States = input().split()
input()
input()
TransitionMatrix = dict()
for S in States:
    TransitionMatrix[S] = dict(zip(States, list(map(log2float, input().split()[1:]))))
input()
input()
EmissionMatrix = dict()
for S in States:
    EmissionMatrix[S] = dict(zip(Sigma, list(map(log2float, input().split()[1:]))))

print("Transition Matrix")
pprint(TransitionMatrix)
print()
print("Emissions Matrix")
pprint(EmissionMatrix)

# X = 'GGCACTGAA'
# Sigma = ['A', 'C', 'G', 'T']
# States = ['B', 'H', 'L']
# TransitionMatrix = {
#     'B': { 'H': log2(.5), 'L': log2(.5) },
#     'H': { 'H': log2(.5), 'L': log2(.5) },
#     'L': { 'H': log2(.4), 'L': log2(.6) }
# }

# EmissionMatrix = {
#     'H': { 'A': log2(.2), 'C': log2(.3), 'G': log2(.3), 'T': log2(.2) },
#     'L': { 'A': log2(.3), 'C': log2(.2), 'G': log2(.2), 'T': log2(.3) },
# }

# print("Transition")
# pprint(TransitionMatrix)
# print()
# print("Emission")
# pprint(EmissionMatrix)
# print()

p = {'B': log2(1)}
path = ''

mk = None
for x in X:
    tmk = max(p, key=p.get)
    if mk == None or p[mk] != p[tmk]:
        mk = tmk
    mv = p[mk]
    for s in States:
        p[s] = mv + TransitionMatrix.get(mk, dict()).get(s, -inf) + EmissionMatrix.get(s, dict()).get(x, -inf)

    tmk = max(p, key=p.get)
    if p[mk] != p[tmk]:
        mk = tmk
    path += mk

    pprint(p)

print(path)

# https://personal.utdallas.edu/~prr105020/biol6385/2018/lecture/Viterbi_handout.pdf