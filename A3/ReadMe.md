# A3 - Operon Predictor

## Script Information

- **Author**: Jay Annadurai
- **Date**: 22 March 2024
- **Programming Language & Version**: Python 3.11
- **Project Version**: 1.0

## Description

The JA-A3 Operon Prediction script is dedicated to analyzing PTT files and predicting operons.
Operons are specified as adjacent co-directional genes with intervening distances less than 50 bp.
Four bacteria PTT files are initially uncompressed and then analyzed. A crop microbiome file is also analyzed.
Both analyses use a similar algorithim to predict operons.

## Script Tasks
The A3-OperonPredictor script was developed to solve the following tasks:
1) Read Bacteria PTT files as Pandas Dataframes and prime the data for analysis tasks
2) Create an algorithim for operon prediction given strand and gene position information
3) Apply the algorithim to the Bacteria PTT files and predict operons for each bactera species
4) Read Crop Microbiome GFF file as a Pandas Dataframe and prime the data for analysis
5) Perform exploratory analysis of the Crop Microbiome data to understand opportunies for Operon prediciton
6) Apply a modified algorithim to the Crop Microbiome data and predict operons
7) Save the outputs of both the standard operon prediction of Bacteria and the adjusted Crop Microbiome

<hr>

## Core Dependencies

- **```Pandas```**: For data reading and manipulation.
- **```Numpy```** & **```Scipy```**: For numerical computations and statistical methods.
- **```Matplotlib```** & **```Seaborn```**: For generating data visualizations.
- **```JayUtilities```**: Contains Utility Functions utilized within the script [In Directory as ```JayUtilities.py```]

## Utility Dependencies
- **```os```**: File Manipulation
- **```gzip```**: Allows for decompression of GZip Files
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
conda create --name JA3_OperonPrediction python=3.11 pandas seaborn matplotlib numpy scipy
conda activate JA3_OperonPrediction
```

The script ```Setup.py``` can be used to decompress the original PTT ```gz``` files in the Source folder. 
The script will place the uncompressed versions in the input folder
The script is not needed for the already uncompressed Crop microbiome GFF file.

The Jupyter notebook ```A3-OperonPredictor.ipynb``` contains the script to predict operons given the input data.
It also reveals data at the various stages of processing to provide insight into the methodology of operon prediciton.

<hr>

## Input Data:
- Input Files:
    - ```B_subtilis_168.ptt```
    - ```E_coli_K12_MG1655.ptt```
    - ```Halobacterium_NRC1.ptt```
    - ```Synechocystis_PCC6803_uid159873.ptt```
- **Desc**: Protein Table Files of various Prokaryotes 
- **Format**: Protein Table (PTT) Files
- **File Location**: Stored within the ```Source``` folder


- Input File: ```2F2088090036.gff```
- **Desc**: Crop microbiome from Hoatzin (IMG ID 2088090036 as obtained from http://img.jgi.doe.gov/cgi-
  bin/m/main.cgi)
- **Format**: General Feature Format (GFF) File
- **File Location**: Stored within the ```Input``` folder
    
## Output Data
- **Output Files**:
  - ```PredictedOperons_Bsubtilis.tsv```
  - ```PredictedOperons_Ecoli.tsv```
  - ```PredictedOperons_Halobacterium.tsv```
  - ```PredictedOperons_Synechocystis.tsv```
- **Desc**: Dataframes with the original gene data with a column of predicted operons
- **Format**: Tab-Separated Value (TSV) Files
- **File Location**: Stored within the ```Output``` folder


- **Output File**: ```PredictedOperons_Crop_Microbimome.tsv```
- **Desc**: Dataframe with the original contig data and predicted operons
- **Format**: Tab-Separated Value (TSV) File
- **File Location**: Stored within the ```Input``` folder

*Both Input Files and Output Path are Configurable at the start of the script*

<hr>

<br><br>

### Original Assignment:
Predict the operons (defined as longest contigous multi-gene
transcriptional units) using the PTT files (attached) for the
following genomes. (Tip: adjacent co-directional genes with
intervening distance less than 50bp can be considered to be in
the same operon)

1) Escherichia coli K12
2) Bacillus Subtilis
3) Halobacterium
4) Synechocystis 


Now predict the operons in a Crop microbiome from Hoatzin (IMG
id 2088090036 obtained from http://img.jgi.doe.gov/cgi-
bin/m/main.cgi) using the attached gff file (which is equivalent to
ptt file although not identical). The first column comprises of the
contig with the fourth and fifth columns comprising the gene start
and stops.C would yield two occurrences of A, two occurrences of G and one occurrence of C at the mono-nucleotide level. Likewise, one occurrence each for AG, GG, GA and AC di-nucleotides when you count for adjacent overlapping nucleotides.