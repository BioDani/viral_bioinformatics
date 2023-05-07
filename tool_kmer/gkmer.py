import itertools
import re

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

def get_all_kmers(k):
    bases = ['A','C','G','T']
    all_kmer_list = [ ''.join(i) for i in list(itertools.product(bases, repeat= k))]
    return all_kmer_list

def get_canonical_kmers(k):
    canonical_kmer_list = []

    for i in get_all_kmers(k):
        temporal = []
        temporal.append(i)
        temporal.append(generate_reverse_complement(i))
        canonical_kmer = sorted(temporal)[0]
        if canonical_kmer not in canonical_kmer_list:
            canonical_kmer_list.append(canonical_kmer)
    return canonical_kmer_list


def validate_seq(seq):
    if re.search(r'^[ACGT]+$', seq):
        return True
    else:
        return False

def get_kmer_count(seq,k):
    seq  = seq.upper()
    total = 0 
    counter = { i: 0 for i in get_canonical_kmers(k)}

    for i in range(len(seq)):
        if len(seq[i:i+k]) == k and validate_seq(seq[i:i+k]):
            total += 1
            temporal = []
            temporal.append(seq[i:i+k])
            temporal.append(generate_reverse_complement(seq[i:i+k]))
            canonical = sorted(temporal)[0]
            counter[canonical] += 1

    counter = { canonical : round(counter[canonical]/total,3) for canonical in counter}
    return counter

def get_kmer_from_csv(path_csvfile,k):
    with open( path_csvfile,'r') as csvfile:
        new_path = path_csvfile.replace(".csv",'_'+str(k)+'mer.csv')
        with open(new_path, 'a+') as newfile:
            header = next(csvfile).replace('\n','') +';;;'+ ";;;".join(get_canonical_kmers(k))+'\n'
            newfile.write(header)
            for i in csvfile:
                i = i.replace('\n','')
                seq = i.split(';;;')[2]
                values = list(get_kmer_count(seq,k).values())
                values = ';;;'.join(str(numero) for numero in values)
                newfile.write(i+';;;'+values+'\n')