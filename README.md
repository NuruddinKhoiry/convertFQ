# convertFQ
Converting DNA to RNA or RNA to DNA in a fastq file

## Example usage

### 1. Convert DNA to RNA
Converting T (thymine) with U (uracil)

$ convertFQ -i INPUT.fastq -c "dna2rna" -o OUTPUT


### 2. Convert RNA to DNA
Converting U (uracil) with T (thymine)

$ convertFQ -i INPUT.fastq -c "rna2dna" -o OUTPUT
