# A4 - Predictor with PSWM

## Script Information

- **Author**: Jay Annadurai
- **Date**: 12 Apr 2024
- **Programming Language & Version**: Python 3.11
- **Project Version**: 1.0

## Description

The JA-A4 Prediction with PSWM script is designed to develop a PSWM given a counts matrix.
It then applies the PSWM to given sequencing information to identify regions of high similarity.

## Script Tasks
The A4-PSWMPredictor script was developed to solve the following tasks:
1) Import argR-binding motif-representing Counts Matrix
2) Build a psuedocount-adjusted Frequency Matrix from the Counts Matrix
3) Compute the PSSM/PSWM/PWM Matrix as the log odds ratio of frequency / expected frequency
4) Import sequencing data of E coli gene upstream regions (400 genes before | 50 genes after)
5) Format the sequencing data into a data frame of Gene IDs and the corresponding sequence
6) Iterate through the sequences and score all segments with the PSWM
7) Identify the top 30 Gene IDs based on the score from the PSWM Matrix

<hr>

## Core Dependencies

- **```Pandas```**: For data reading and manipulation.
- **```Numpy```** & **```Scipy```**: For numerical computations and statistical methods.
- **```Matplotlib```** & **```Seaborn```**: For generating data visualizations.
- **```JayUtilities```**: Contains Utility Functions utilized within the script [In Directory as ```JayUtilities.py```]

## Utility Dependencies
- **```os```**: File Manipulation
- **```gzip```**: Allows for decompression of GZip Files
- **```bz2```**: Allows for decompression of BZip Files
- **```shutil```**: Allows for file transfer of files
- **```sys```**: Allows for environmental path adjustment to import files
- **```JayUtilities```**: Contains Utility Functions utilized within the script [In Directory as ```JayUtilities.py```]

## Optional Dependencies
- **```PPrint```**: For Pretty Printing Data
- **```openpyxl```**: Allows reading of Excel Files

<hr>

## Execution

Ensure you have Python 3.11 installed in your Conda environment. 
Install the required dependencies using Conda by running the following commands in your terminal:

```bash
conda create --name JA4-PSWMPredictor python=3.11 pandas numpy scipy seaborn matplotlib
conda activate JA4-PSWMPredictor
```

The script ```Setup.py``` can be used to decompress the original ```bz``` files in the Source folder. 
The script will place the uncompressed versions in the input folder
The script is not needed for the already uncompressed argR-counts-matrix.tx.

The Jupyter notebook ```A4-PSMPredictor.ipynb``` contains the script to predict operons given the input data.
It also reveals data at the various stages of processing to provide insight into the methodology of operon prediciton.

<hr>

## Input Data:
- Input Files:
    - ```E_coli_K12_MG1655.400_50.bz2```
- **Desc**: 400 upstream bases and 50 downstream bases of selected E coli genes presented in FASTA nucleotide format
- **Format**: FASTA Nucleotide Text
- **File Location**: Stored within the ```Source``` folder


- Input File: ```argR-counts-matrix.txt```
- **Desc**: Counts Matrix of a Motif that binds argR Transcription Factor
- **Format**: Tab-Separated Value (TSV) Files
- **File Location**: Stored within the ```Input``` folder
    
## Output Data
- **Output Files**:
  - ```ArgR-Motif-PSWM.tsv```
  - ```Gene_Binding_Site_Evaluations_Top30.tsv```
  - ```Gene_Binding_Site_Evaluations_All.tsv```
- **Desc**: Dataframes with the corresponding information
- **Format**: Tab-Separated Value (TSV) Files
- **File Location**: Stored within the ```Output``` folder

*Both Input Files and Output Path are Configurable at the start of the script*

<hr>

<br><br>

### Original Assignment:
In motif finding, a weight matrix (also referred to as Position Weight Matrix
or Position Specific Weight Matrix) is defined as the log-odds matrix whose
elements are defined as

W (b, j) = log ( F’ (b, j) / F(b, o) )

Where b corresponds to the base and j is the index accounting for the
number of bases in the motif. F’ (b, j) corresponds to the frequency with
which each base occurs at a specified position and can easily be calculated
from the counts matrix after adjusting for zero values (see below). F(b, o)
corresponds to the background frequency with which a particular base is
known to occur and can be assumed to be 0.25 for all bases at all positions in
the motif.

A transcription factor argR is known to bind to a motif which can be
represented with the following counts matrix built from a total of 27 binding
sites documented in the literature (the counts matrix is attached as a text file
which should be used by your program).

Now write a script/program to compute the frequency matrix F( b, j) using
the above counts matrix. Since log odds matrix is based on frequency
matrix, to avoid taking logarithm of 0 in computing it, a revised F’ (b, j) can
be computed by augmenting all the base counts in counts matrix by 1
thereby artificially increasing the number of sites to 31 (put another way, a
pseudocount of +1 is added to each of the real counts for each base at each
position, which increases the total counts at each position in the matrix to
31). Based on this notion, compute the F’ (b, j) as well in the same
script/program.

Now use the weight matrix to scan and identify the binding sites in the
attached set of upstream regulatory regions of genes by filtering to those
with highest similarity to the PSM i.e, your program should predict and
show only the top 30 scoring gene ids corresponding to these sequences.
Upstream regulatory regions of genes defined as 400 bases upstream and 50
bases after the translational start site are provided in the fasta nucleotide
format along with information about the gene id to which it corresponds to.