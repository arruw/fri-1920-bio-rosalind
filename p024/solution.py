from math import log2, inf
from pprint import pprint
import operator

def readFasta(filePath):
    fasta = {}
    label = None
    with open(filePath, 'r') as file:
        for line in file:
            line = line.replace('\n', '').replace('\r', '')
            if line.startswith('>'):
                label = line.replace('>', '')
            else:
                fasta[label] = fasta.get(label, '') + line
    return fasta

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
from Bio.Seq import Seq 

seqs = list(map(lambda x: x[1], readFasta('p024/input.txt').items()))

alignments = pairwise2.align.localds(seqs[0], seqs[1], MatrixInfo.pam250, -5, -5)

for a in alignments:
    print(int(a[2]))
    print(a[0][a[3]:a[4]].replace('-', ''))
    print(a[1][a[3]:a[4]].replace('-', ''))
    # print()
    # print(format_alignment(*a, full_sequences=True))
    print('================================================')