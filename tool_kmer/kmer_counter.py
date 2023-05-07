import kmer
import rc

def get_kmer_count(seq,k):
    seq  = seq.upper()
    total = 0 
    counter = { i: 0 for i in kmer.get_canonical_kmers(k)}

    for i in range(len(seq)):
        if len(seq[i:i+k]) == k:
            total += 1
            temporal = []
            temporal.append(seq[i:i+k])
            temporal.append(rc.generate_reverse_complement(seq[i:i+k]))
            canonical = sorted(temporal)[0]
            counter[canonical] += 1

    counter = { canonical : round(counter[canonical]/total,3) for canonical in counter}
    return counter