# A1 - Matrices

## Script Information

- **Author**: Jay Annadurai
- **Date**: 14 February 2024
- **Programming Language & Version**: Python 3.11
- **Project Version**: 1.0

## Description

The "A1 - Matrices" script is designed to analyze gene expression data quantified in Reads Per Kilobase Million (RPKM) of microRNAs across various cancer classes. It reads input data from tab-separated values (TSV) files, generates Pearson correlation matrices, visualizes these matrices as heatmaps, and compares the matrices between the two datasets with a Pearson Correlation Coefficient. This tool aims to reveal similarities and differences in miRNA expression across cancer types, facilitating a deeper understanding of cancer biology.

## Dependencies

- **Pandas**: For data reading and manipulation.
- **Seaborn**: For generating advanced data visualizations, specifically heatmaps.
- **Matplotlib**: For basic data visualization.
- **Numpy**: For numerical computations.

## Installation

Ensure you have Python 3.11 installed in your Conda environment. Install the required dependencies using Conda by running the following commands in your terminal:

```bash
conda create --name myenv python=3.11 pandas seaborn matplotlib numpy
conda activate myenv
```

## Input Data: 
  - Gene Expression Matrices (```matrix1.txt``` & ```matrix2.txt```)
    - **Desc**: Gene expression data quantified in RPKM of microRNAs among various classes of cancer
    - **Format**: Tab-Separated Value (TSV) files
    - **File Location**: Stored within the ```data``` folder
    
## Output Data
- Correlation Heatmaps of Gene Expression Matrices (```correlation_matrix1_heatmap.png``` & ```correlation_matrix2_heatmap.png```)
    - **Desc**: Seaborn Heatmaps generated from the Correlation Matrices generated from the Original Matrices
    - **Format**: PNG (Portable Network Graphic) Images
    - **File Location**: Stored within the ```output``` folder

*Both Input Files and Output Path are Configurable*

## Assignment Description
The script was developed to solve the following tasks:

1. Generate a 12 x 12 Pearson correlation matrix for each miRNA expression across different cancer types dataset.
2. Visualize these matrices as heatmaps to reveal similarities between cancers.
3. Compute a Pearson correlation between the two original matrices to compare datasets directly.