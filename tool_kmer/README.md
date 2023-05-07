# Kmers Generator  

k-mers are substrings of length k contained within a biological sequence. 

This tool allows to generate of the kmers of a sequence that is inside the third column of a CSV file. 



## Use

To run this tool run:

1. Have a `CSV_FILE`  separated by `;;;` with the following structure.


| Column Name| Description     | Example                |
| :-------- | :------- | :------------------------- |
| `id` | Unique ID of sequence   | `9d13b0ff-66f3-4dc8-a5ad-89fff01652bb` |
| `name_seq` | Original name of sequence | `seq1` |
| `seq` | DNA or RNA sequence | `GCTAGCTAGCTAGCTAGCGTAGCTAGCTAGCTAGCTAGCTACGATCGTACTAGCTAGCTGGTAGCTAGCTAGCTAGCTAGCTAGCTGCTAGCGTAGCTAGCTAGCTAGCTAGCTAGCA` |

2. Import the module

```python
  import gkmer
```

3. Run this function
```python
  gkmer.get_kmer_from_csv(CSV_FILE, length_kmer)
```
| Param|  Description    | Example                |
| :-------- | :------- | :------------------------- |
| `CSV_FILE` |  File with 3 columns separated by `;;;`| `example.csv`|
| `length_kmer` | Length of the kmer required | `2`,`3`,`4`,...,n|

4. Review the output CSV file with the proportion of each kmer of a sequence.

| Length Kmer|  Number of kmer generated|                 
| :-------- | :------- | 
| 2 | 10 |
| 3 | 32 | 
| 4 | 136 | 
| 5 | 512 | 


**Note:** The `length_kmer` will depend on the computing power you have available on your computer. 


## Author

- Github: [BioDani](https://www.github.com/BioDani)

- LinkedIn: [Daniel Tejada](https://www.linkedin.com/in/dtejadah)


