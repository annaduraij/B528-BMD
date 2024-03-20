# A2 - HalfLives

## Script Information

- **Author**: Jay Annadurai
- **Date**: 22 February 2024
- **Programming Language & Version**: Python 3.11
- **Project Version**: 1.0

## Description

The "A2 - HalfLives" script is dedicated to analyzing timecourse experiments of yeast open reading frame (YORF) products. It calculates the half-lives of transcripts from three sets of time series data provided in 'DecayTimecourse.txt'. The script computes the half-lives for each transcript, averages them across three replicates, and identifies genes with significantly high (top 10%) and low (bottom 10%) half-lives. It selects the aforementioned genes and outputs them as a CSV for simple functional enrichment analysis using GO annotations, aiding in understanding the biological significance of these genes.
## Dependencies

- **Pandas**: For data reading and manipulation.
- **Matplotlib & Seaborn**: For generating data visualizations.
- **Numpy & Scipy**: For numerical computations and statistical methods.

## Installation

Ensure you have Python 3.11 installed in your Conda environment. Install the required dependencies using Conda by running the following commands in your terminal:

```bash
conda create --name HalfLivesEnv python=3.11 pandas seaborn matplotlib numpy scipy
conda activate HalfLivesEnv
```

## Input Data: 
  - Yeast Open Reading Frame Expression Data (```DecayTimeCourse.txt```)
    - **Desc**: YORF Expression Time Series Data for 3 Different Timecourses
    - **Format**: Tab-Separated Value (TSV) Text file
    - **File Location**: Stored within the ```data``` folder
    
## Output Data
- Lists of YORFs (```Top10_YORFs.csv``` & ```Bot10_YORFs.csv```)
    - **Desc**: Filtered Output of a Pandas Dataframe containing the 10% Extreme in terms of Average Half Lives among the Measured YORFs
    - **Format**: Comma-Separated Value (CSV) file
    - **File Location**: Stored within the ```output``` folder

*Both Input Files and Output Path are Configurable*

## Assignment Description
The script was developed to solve the following tasks:

1. Preparing a source of data for analysis by restructuring it into an optimal format
2. Handle, validate, and sanitize time series data of YORFs for transformation with natural log prior to regression
3. Apply linear regression and solve for the rate constant per YORF
4. Calculate Half-Lives per YORF computationally across all three Time Courses
5. Filter YORFs by top 10% and bottom 10% and output in a suitable format for simple functional enrichment analysis with the following tools:
    - http://biit.cs.ut.ee/gprofiler/ 
    - http://go.princeton.edu/cgi-bin/GOTermFinder