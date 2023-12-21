from loading import load_directory
from kmers import stream_kmers, kmer2str
import numpy as np
from matplotlib import pyplot as plt
import heapq
import math

def xorshift(x):
    x ^= (x << 13) & 0xFFFFFFFFFFFFFFFF
    x ^= (x >> 7) & 0xFFFFFFFFFFFFFFFF
    x ^= (x << 17) & 0xFFFFFFFFFFFFFFFF
    return x

def echantillonage(fileA,k,s):
    sketch = [-math.inf]*s
    heapq.heapify(sketch)
    for i in range(len(fileA)):
        for kmer in stream_kmers(fileA[i],k):
            new_kmer = xorshift(kmer)
            elem = sketch[0]
            if new_kmer > elem:
                heapq.heappop(sketch)
                heapq.heappush(sketch, new_kmer)
    return sketch


def jaccard_heap(listeA, listeB):
    listeA.sort()
    listeB.sort()
    I = 0
    U = 0
    i=0
    j=0
    while i <len(listeA) and j<len(listeB):
        if listeA[i] == listeB[j]:
            U += 1
            I += 1
            i += 1
            j += 1
        else:
            U +=1
            if listeA[i] < listeB[j]:
                i +=1
            else:
                j +=1
    return I/U

if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("C:/Users/dcnad/Downloads/data")
    k = 31
    s = 5000
    filenames = list(files.keys())
    mat = np.zeros((5,5))
    heap_lists = []
    for i in range(len(files)):
        heap_lists.append(echantillonage(files[filenames[i]],k,s))
    for i in range(len(files)):
        mat[i,i] = 1
        for j in range(i+1, len(files)):
            J = jaccard_heap(heap_lists[i], heap_lists[j])
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
    #fig.savefig('C:/Users/dcnad/Downloads/matrixbact_heap.png', bbox_inches = 'tight') 
    plt.show()
