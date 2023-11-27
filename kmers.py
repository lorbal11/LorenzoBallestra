
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for i in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)


def stream_kmers(seq, k):
    x = 0
    y = 0
    mask = (1<<(k*2))-1
    for nuc in range(0,len(seq)):
        if seq[nuc] not in ["A","C","T","G"]:
            pass
        else:
            n = (ord(seq[nuc])>>1)%4
            x <<=2
            x += n
            x&=mask
            if nuc < k-1:
                y += ((n-2)%4)<<((nuc+1)*2)
            else:
                y >>=2
                y += ((n-2)%4)<<((k-1)*2)
                yield min(x,y)
