from loading import load_directory
from kmers import stream_kmers, kmer2str
import numpy as np



def jaccard(fileA, fileB, k):
    dic = {}
    U = 0
    I = 0
    for w in range(0,len(fileA)):
        for kmer in stream_kmers(fileA[w],k):
            dic[kmer] = 1 if kmer not in dic else dic[kmer]+1
            U +=1
    for w in range(0,len(fileB)):
        for kmer in stream_kmers(fileB[w],k):
            if kmer in dic:
                I +=1
                dic[kmer]= dic[kmer]-1
                if dic[kmer]==0:
                    del dic[kmer]
            else:
                U += 1
    return I/U



if __name__ == "__main__":
    # Load all the files in a dictionary
    files = load_directory("C:/Users/dcnad/Downloads/data")
    k = 21
    filenames = list(files.keys())
    mat = np.zeros((len(files),len(files)))
    for i in range(len(files)):
        mat[i,i] = 1
        for j in range(i+1, len(files)):
            J = jaccard(files[filenames[i]], files[filenames[j]], k)
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
    plt.show()

