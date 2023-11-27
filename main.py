from loading import load_directory
from kmers import stream_kmers, kmer2str



def jaccard(fileA, fileB, k):
    dic = {}
    U = 0
    I = 0
    for w in range(0,len(fileA)):
        for kmer in enum(fileA[w],k):
            dic[kmer] = 1 if kmer not in dic else dic[kmer]+1
            U +=1
    for w in range(0,len(fileB)):
        for kmer in enum(fileB[w],k):
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
    files = load_directory("data")
    k = 21
    
    filenames = list(files.keys())
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            
            # --- Complete here ---

            j = jaccard(files[filenames[i]], files[filenames[j]], k)
            print(filenames[i], filenames[j], j)
