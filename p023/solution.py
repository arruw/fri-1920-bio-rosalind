from math import log2, inf
from pprint import pprint
import operator

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
from Bio.Seq import Seq 

input()
seq1 = Seq(input())
input()
seq2 = Seq(input())

alignments = pairwise2.align.globalds(seq1, seq2, MatrixInfo.blosum62, -5, -5)

for a in alignments:
    print(format_alignment(*a))