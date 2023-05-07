import kmer
import kmer_counter

def get_kmer_from_csv(path_csvfile,k):
    with open( path_csvfile,'r') as csvfile:
        new_path = path_csvfile.replace(".csv",'_'+str(k)+'mer.csv')
        with open(new_path, 'a+') as newfile:
            header = next(csvfile).replace('\n','') +';;;'+ ";;;".join(kmer.get_canonical_kmers(k))+'\n'
            newfile.write(header)
            for i in csvfile:
                i = i.replace('\n','')
                seq = i.split(';;;')[2]
                values = list(kmer_counter.get_kmer_count(seq,k).values())
                values = ';;;'.join(str(numero) for numero in values)
                newfile.write(i+';;;'+values+'\n')