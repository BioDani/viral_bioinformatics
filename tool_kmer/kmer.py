import itertools
import rc

def get_all_kmers(k):
    bases = ['A','C','G','T']
    all_kmer_list = [ ''.join(i) for i in list(itertools.product(bases, repeat= k))]
    return all_kmer_list

def get_canonical_kmers(k):
    canonical_kmer_list = []

    for i in get_all_kmers(k):
        temporal = []
        temporal.append(i)
        temporal.append(rc.generate_reverse_complement(i))
        canonical_kmer = sorted(temporal)[0]
        if canonical_kmer not in canonical_kmer_list:
            canonical_kmer_list.append(canonical_kmer)
    return canonical_kmer_list