from loading import load_directory
from kmers import stream_kmers, kmer2str
import numpy as np
from matplotlib import pyplot as plt
import math

def xorshift(x):
    x ^= (x << 13) & 0xFFFFFFFFFFFFFFFF
    x ^= (x >> 7) & 0xFFFFFFFFFFFFFFFF
    x ^= (x << 17) & 0xFFFFFFFFFFFFFFFF
    return x

def ech_hash(fileA,k,s):
    sketch = [-math.inf]*s
    for j in range(len(fileA)):
        for kmer in stream_kmers(fileA[j],k):
            new_kmer = xorshift(kmer)
            i = new_kmer%s
            sketch[i] = max(sketch[i], new_kmer)
    return sketch


def jaccard_hash(listeA, listeB):
    U = 0
    I = 0
    for i in range(len(listeA)):
        if listeA[i] == listeB[i]:
            U += 1
            I += 1
        else:
            U += 2
    return I/U


if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("C:/Users/dcnad/Downloads/data")
    k = 31
    s = 5000
    filenames = list(files.keys())
    mat = np.zeros((5,5))
    hash_lists = []
    for i in range(len(files)):
        hash_lists.append(ech_hash(files[filenames[i]],k,s))
    for i in range(len(files)):
        mat[i,i] = 1
        for j in range(i+1, len(files)):
            J = jaccard_hash(hash_lists[i], hash_lists[j])
            mat[i,j] = J
            mat[j,i]= J
            print(filenames[i], filenames[j], J)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(mat)
    fig.colorbar(cax)
    ax.set_xticks(range(len(files)))
    ax.set_yticks(range(len(files)))
    ax.set_xticklabels(filenames, rotation=-70)
    ax.set_yticklabels(filenames)
    fig.savefig('C:/Users/dcnad/Downloads/matrixbact_hash.png', bbox_inches = 'tight') 
    plt.show()

