import uuid

def create_fasta_to_csv(path):
    sequences = {}
    with open( path, 'r' ) as fasta:
        for line in fasta:
            flag = 1
            if '>' in line:
                flag = 0
                id = str(uuid.uuid4())
                name_seq = line.replace('>','').replace('\n','')
                seq = ''

                sequences[id]={'name_seq':name_seq,'seq':seq}

            if (flag == 1) and ('>' not in line): 
                seq += line.replace('\n','').replace(' ','')
                sequences[id]={'name_seq':name_seq,'seq':seq}

    fasta_path = path.replace('.fasta','.csv')

    with open( fasta_path, 'a') as newfile:
        newfile.write('id;;;name_seq;;;seq\n')
        for i in sequences:
            newfile.write(str(i)+';;;'+sequences[i]['name_seq']+';;;'+sequences[i]['seq']+'\n')
        print('Status: Completed.')