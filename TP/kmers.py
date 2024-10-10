
def kmer2str(val, k):
    """ Transform a kmer integer into a its string representation
    :param int val: An integer representation of a kmer
    :param int k: The number of nucleotides involved into the kmer.
    :return str: The kmer string formatted
    """
    letters = ['A', 'C', 'T', 'G']
    str_val = []
    for _ in range(k):
        str_val.append(letters[val & 0b11])
        val >>= 2

    str_val.reverse()
    return "".join(str_val)

kmer_str = kmer2str(50, 3)
print("kmer_str:", kmer_str) #kmer_str: GAT


def encode_nucl(letter):
    encoding = {'A': 0, 'C': 1, 'T': 2, 'G': 3}
    return encoding[letter]


def encode_kmer(kmer_str, k):
    kmer_int = 0
    for letter in kmer_str[0:k]:
        kmer_int <<= 2  
        kmer_int += encode_nucl(letter)  
    return kmer_int

kmer_str_to_int = encode_kmer("GAT", 3)
print("seq_encode", kmer_str_to_int) #seq_encode 50


def enumerate_kmers(seq, k):
    kmer_count = {}
    kmer = encode_kmer(seq, k)  
    mask = (1 << (2 * k)) - 1   

    for i in range(len(seq) - k + 1):

        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1


        if i + k < len(seq):
            kmer <<= 2                
            kmer &= mask          
            kmer += encode_nucl(seq[i + k])  
    return kmer_count

enumerate_kmers_ex = enumerate_kmers("AATA", 3)
print("enumerate_kmers_ex", enumerate_kmers_ex) #enumerate_kmers_ex {2: 1, 8: 1}

