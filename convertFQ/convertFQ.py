from Bio import SeqIO
from Bio import Seq
import argparse


parser = argparse.ArgumentParser(description='convertFQ: RNA -> DNA | DNA -> RNA')
parser = argparse.ArgumentParser(prog='convertFQ')
parser.add_argument("-v", '--version', action='version', version='%(prog)s v.1.0')
parser.add_argument("-i", "--input", required=True, help="Input FASTQ [Required]")
parser.add_argument("-c", "--conversion", required=True, type=str, help="rna2dna | dna2rna [Required]")
parser.add_argument("-o", "--output", required=True, type=str, help="output name [Required]")
args = vars(parser.parse_args())

if args['conversion'] == 'rna2dna':
    print('Converting RNA to DNA ...\n')
    new_records = []
    for record in SeqIO.parse(args['input'], "fastq"):
        sequence = str(record.seq)
        letter_annotations = record.letter_annotations

        # You first need to empty the existing letter annotations
        record.letter_annotations = {}

        new_sequence = sequence.replace('U','T')
        record.seq = Seq.Seq(new_sequence)


        new_letter_annotations = {'phred_quality': letter_annotations['phred_quality']}
        record.letter_annotations = new_letter_annotations

        new_records.append(record)

    with open(str(args['output'])+'.fastq', 'w') as output_handle:
        SeqIO.write(new_records, output_handle, "fastq")
        
elif args['conversion'] == 'dna2rna':
    print('Converting DNA to RNA ...\n')
    new_records = []
    for record in SeqIO.parse(args['input'], "fastq"):
        sequence = str(record.seq)
        letter_annotations = record.letter_annotations

        # You first need to empty the existing letter annotations
        record.letter_annotations = {}

        new_sequence = sequence.replace('T','U')
        record.seq = Seq.Seq(new_sequence)


        new_letter_annotations = {'phred_quality': letter_annotations['phred_quality']}
        record.letter_annotations = new_letter_annotations

        new_records.append(record)

    with open(str(args['output'])+'.fastq', 'w') as output_handle:
        SeqIO.write(new_records, output_handle, "fastq")
else:
    print('Sorry '+str(args['conversion'])+' is wrong option\nPlease use eihter "rna2dna" or "dna2rna"') 