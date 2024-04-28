# PQ - B528 Programming Quiz

## Script Information

- **Author**: Jay Annadurai
- **Date**: 20 March 2024
- **Programming Language & Version**: Python 3.11
- **Project Version**: 1.0

## Description

The "PQ" script is dedicated to analyzing two RNA sequences for differences in dinucleotide and trinucleotide frequencies. It also reverse transcribes them into DNA. Note, ChatGPT was used to assist with some BioPython syntax.

## Core Dependencies

- **```Pandas```**: For data reading and manipulation.
- **```Biopython```**: For reading and interpreting FASTA sequences
- **```Numpy``` & ```Scipy```**: For numerical computations and statistical methods.
- **```JayUtilities```**: Contains Utility Functions utilized within the script [Stored in directory as ```JayUtilities.py```]

## Utility Dependencies
- **```os```**: File Manipulation
- **```JayUtilities```**: Contains Utility Functions utilized within the script [Stored in directory as ```JayUtilities.py```]
- 
## Optional Dependencies
- **```PPrint```**: For Pretty Printing Data
- **```openpyxl```**: Allows reading of Excel Files

## Installation

Ensure you have Python 3.11 installed in your Conda environment. Install the required dependencies using Conda by running the following commands in your terminal:

```bash
conda create --name ProgammingQuizEnv python=3.11 pandas seaborn matplotlib numpy scipy
conda activate ProgammingQuizEnv
```

## Input Data: 
  - Input Files (```RNA-sequence1.fna``` & ```RNA-sequence2.fna```)
    - **Desc**: RNA Sequences
    - **Format**: Sequence Files in FASTA format
    - **File Location**: Stored within the ```Input``` folder
    
## Output Data
- Output Files (```Dinucleotide DF.tsv``` & ```Signficant Dinucleotides.tsv``` & ```Trinucleotide DF.tsv``` & ```Signficant Trinucleotides.tsv```)
    - **Desc**: Dataframes with counts and frequencies of RNA dinucleotides and trinucleotides with filtered views where the difference ratio exceeded 3 in the form of the Significant TSVs
    - **Format**: Tab-Separated Value (TSV) file
    - **File Location**: Stored within the ```Output``` folder

*Both Input Files and Output Path are Configurable at the start of the script*

## Assignment Description
The script was developed to solve the following tasks:
1) Take two input RNA strands and reverse transcribe into DNA
2) Print Absolute Frequency and Percentage of RNA dinucleotides of each original RNA strand
3) Print Absolute Frequency and Percentage of RNA trinucleotides of each original RNA strand
4) Compare the percent frequency of both RNA dinucleotides and RNA trinucleotides between the two RNA strands and Identify RNA dinucleotides and RNA trinucleotides that have 3-fold change (3x change)

## Original Assignment:
Sometimes information flows from RNA to DNA such as when you convert RNA into cDNA molecules for microarray analysis or for what we commonly call as RNA-sequencing using an illumina sequencer. Write a program to reverse transcribe RNA to DNA for the two fasta RNA sequence files (RNA-sequence1.fna and RNA-sequence2.fna). Print only the forward strand from 5’ to 3’ for each of the two reverse transcribed molecules. Please also compute the di-nucleotide and tri-nucleotide frequency (both absolute and percentage) of the nucleotides present in the original RNA sequences in the two files. The output should be in the following three column format for each pair of RNA base combinations for each input file:





Now use this program to compare the differences in the percentage abundance of a dinucleotide and trinucleotide composition between the two sequences (in the above fasta files) to identify those, which differ by three fold (3X times) in percentage between pairs of sequences that are provided.
Hint: There are a total of  16 combinations of dinucleotides and 64 combinations of trinucleotides in an RNA sequence. Measurements are computed by scanning for overlapping nucleotides as shown in the below example

AGGAC would yield two occurrences of A, two occurrences of G and one occurrence of C at the mono-nucleotide level. Likewise, one occurrence each for AG, GG, GA and AC di-nucleotides when you count for adjacent overlapping nucleotides.