# Conversor of Virus' GenBank file to CSV and Fasta file 

it receives a Virus' GenBank(Full) file that contains one or more locus(virus) and generates two new files with relevant informatión of these virus: a fasta and a csv file





## Use

To run this tool run:

1. Have a GenBank file

```python
  GenBankFile = 'example.gb'
``` 

2. Import the module

```python
  import gbfile
```

2. Run this function
```python
  gbfile.create_file_from_gbfile(GenBankFile)
```

3. Review the output CSV file

| Column Name| Description     | Example                |
| :-------- | :------- | :------------------------- |
| `locus` |  the locus name is the accession number of GenBank. The locus name is usually the first letter of the genus and species names, followed by the accession number | `NC_011620` |
| `family` | Virus Family   | `Alphaflexiviridae` |
| `genus` | Virus Genus   | `Potexvirus` |
| `host` | Relationship between virus and its hosts   | `null` |
| `NucleicAc_type` | Baltimore classification   | `ss-RNA` |
| `long` | Long of DNA or RNA   | `6435` |
| `date` | Publication date   | `13-AUG-2018` |
| `country` | Country where it was found  | `Colombia` |
| `pubmed` | Pubmed code, relation with articles   | `3404114` |
| `segment` | Segment of multipartite virus  | `null` |
| `seq` | Sequence of DNA or RNA   | `ACAAGCATCGATGCTAGCTACGTAGCTA` |

**Note:** The field by default is `null`. 

4. Review the output fasta file. 

Example: 
```python
>NC_011620 Alphaflexiviridae Potexvirus null ss-RNA 6435 13-AUG-2018 Colombia 3404114 null
ACAAGCATCGATGCTAGCTACGTAGCTA
```


**Note:** The file is separated with `;;;`. 



## Author

- Github: [BioDani](https://www.github.com/BioDani)

- LinkedIn: [Daniel Tejada](https://www.linkedin.com/in/dtejadah)


