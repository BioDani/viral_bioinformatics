def reverse(seq):
    return seq[::-1]

def complement(seq):
    comp = {"A":"T","T":"A","C":"G","G":"C"}
    comp_seq = ""
    for base in seq:
        comp_seq += comp[base]
    return comp_seq

def generate_reverse_complement(seq):
    return complement(reverse(seq.upper()))