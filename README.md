# convertFQ: Converting DNA to RNA or RNA to DNA in a fastq file
============================================================

This program is made to help you converting RNA to DNA or DNA to RNA in a fastq file.

### Installation

Download the lastest realese of convertFQ (convertFQ-1.0.tar.gz). Then install it using pip

```bash
$ pip install convertFQ-1.0.tar.gz
```

### Example usage

##### 1. Convert DNA to RNA
Converting T (thymine) with U (uracil)

```bash
$ convertFQ -i INPUT.fastq -c "dna2rna" -o OUTPUT
```


##### 2. Convert RNA to DNA
Converting U (uracil) with T (thymine)

```bash
$ convertFQ -i INPUT.fastq -c "rna2dna" -o OUTPUT
```