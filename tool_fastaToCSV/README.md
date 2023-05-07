
# Fasta file to CSV file conversor 

It receives a fasta file with 1 or n fasta sequences and converts each to a row inside a CSV file.





## Use

To run this tool run:

1. Have a fasta file 

2. Import the module

```python
  import fasta_to_csv
```

2. Run this function
```python
  fasta_to_csv.create_fasta_to_csv(FastaFile)
```

3. Review the output file.

| Column Name| Description     | Example                |
| :-------- | :------- | :------------------------- |
| `id` | Unique ID of sequence   | `9d13b0ff-66f3-4dc8-a5ad-89fff01652bb` |
| `name_seq` | Original name of sequence | `seq1` |
| `seq` | DNA or RNA sequence | `GCTAGCTAGCTAGCTAGCGTAGCTAGCTAGCTAGCTAGCTACGATCGTACTAGCTAGCTGGTAGCTAGCTAGCTAGCTAGCTAGCTGCTAGCGTAGCTAGCTAGCTAGCTAGCTAGCA` |

**Note:** The file is separated with `;;;`. 



## Author

- Github: [BioDani](https://www.github.com/BioDani)

- LinkedIn: [Daniel Tejada](https://www.linkedin.com/in/dtejadah)


