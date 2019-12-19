from math import log2, inf
from pprint import pprint
import operator

from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SubsMat import MatrixInfo
from Bio.Seq import Seq 

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

seqs = list(map(lambda x: x[1], readFasta('p025/input.txt').items()))

alignments = pairwise2.align.globalds(seqs[0], seqs[1], MatrixInfo.blosum62, -11, -1)

for a in alignments:
    print(int(a[2]))
    print(a[0])
    print(a[1])
    # print(format_alignment(*a))