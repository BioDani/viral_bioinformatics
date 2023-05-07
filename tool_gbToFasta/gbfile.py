import re

def create_file_from_gbfile(path):

    # Dictionary statement
    NucleicAc_type={}
    long={}
    date={}
    host={}
    definition={}
    pubmed={}
    country={}
    segment={}
    family={}
    genus={}
    sequences={}
    flag=0
    # list statement
    LOCUS=[]

    with open(path, 'r') as gbfile:
        for line in gbfile:

            line_same = line 
                
            if 'LOCUS' in line:
                line= re.split(r"\s+", line)
                locus=line[1]
                LOCUS.append(locus)
                
                NucleicAc_type[locus]=line[4]
                long[locus]=line[2]
                date[locus]=line[7]
            
            # null values by default for all variables 
                pubmed[locus]= 'null'
                country[locus]= 'null'
                segment[locus]= 'null'
                family[locus]= 'null'
                genus[locus]= 'null'
                host[locus]= 'null'

            if 'DEFINITION' in line:
                line= line.replace('DEFINITION  ','')
                line= line.replace('\n','')
                line=line.split(',')
                if len(line) !=  2:
                    line.append('null')    
                line= line[0].replace(' ','_')
                
                definition[locus]=line
            
            if re.search(r'; \w+viridae', line_same):
                family_temp=re.search('(\w+viridae)', line_same)
                
                family[locus]=family_temp[0]
            
            if re.search(r'; \w+virus.', line_same):
                genus_temp=re.search(r'(\w+virus)', line_same)
                
                genus[locus]=genus_temp[0]

            if '                     /host="' in line:
                line= line.replace('                     /host=','')
                line= line.replace('"','')
                line= line.replace(' ','_')
                line=line.replace('\n','')
                host[locus] = line
                
            if 'PUBMED' in line:
                line1=re.split(r"\s+", line)
                
                pubmed[locus]=line1[2]

            
            if 'country=' in line:
                line=line.replace('                     /country=','')
                line=line.replace('\"','')
                line=line.replace('\n','')
                line= re.split(':', line)
                
                country[locus] = line[0]
                
            if '/segment=' in line:
                line= line.replace(r'/segment=','')
                line=line.replace('"','')
                line=line.replace('RNA 1','RNA1')
                line=line.replace('RNA 2','RNA2')
                line=line.replace('RNA-1','RNA1')
                line=line.replace('RNA-2','RNA2')
                line=line.replace('RNA 3','RNA3')
                line=line.replace('RNA 5','RNA5')
                line=line.replace('RNA 6','RNA6')
                line=line.replace('RNA-3','RNA3')
                line=line.replace('RNA-4','RNA4')
                line=line.replace('RNA-5','RNA5')
                line=line.replace('RNA-6','RNA6')
                line=line.replace('\n','')

                segment[locus]= line

            if 'ORIGIN' in line:
                flag = 1
                sequence= ''
            
            if flag == 1:

                sequence=sequence+line
                sequence=re.sub('ORIGIN','',sequence)
                sequence=re.sub('//','',sequence)
                sequence=sequence.replace('\n','')
                sequence=re.sub('\s+','',sequence)
                sequence=re.sub('[0-9]','',sequence)
                sequence= sequence.upper()
                
            
            if '//' in line:
                sequences[locus]=sequence
                flag = 0

    path_fasta = path.replace('.gb','.fasta')
    with open(path_fasta, 'w') as newfile:
        for locus in LOCUS:
            newfile.write('>'+locus+' '+family[locus]+' '+genus[locus]+' '+host[locus]+' '+NucleicAc_type[locus]+' '+long[locus]+' '+date[locus]+' '+country[locus]+' '+pubmed[locus]+' '+segment[locus]+'\n')
            newfile.write(sequences[locus]+'\n')

    path_csv = path.replace('.gb','.csv')
    with open(path_csv, 'w') as newfile:
        newfile.write('locus;;;family;;;genus;;;host;;;NucleicAc_type;;;long;;;date;;;country;;;pubmed;;;segment;;;seq\n')
        for locus in LOCUS:
            newfile.write(locus+';;;'+family[locus]+';;;'+genus[locus]+';;;'+host[locus]+';;;'+NucleicAc_type[locus]+';;;'+long[locus]+';;;'+date[locus]+';;;'+country[locus]+';;;'+pubmed[locus]+';;;'+segment[locus]+';;;')
            newfile.write(sequences[locus]+'\n')