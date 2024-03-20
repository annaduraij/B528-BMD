# PQ - B528 Programming Quiz

## Script Information

- **Author**: Jay Annadurai
- **Date**: 20 March 2024
- **Programming Language & Version**: Python 3.11
- **Project Version**: 1.0

## Description

The "PQ" script is dedicated to analyzing 

## Core Dependencies

- **```Pandas```**: For data reading and manipulation.
- **```Matplotlib``` & ```Seaborn```**: For generating data visualizations.
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
  - Input File (```DecayTimeCourse.txt```)
    - **Desc**: YORF Expression Time Series Data for 3 Different Timecourses
    - **Format**: Tab-Separated Value (TSV) Text file
    - **File Location**: Stored within the ```Input``` folder
    
## Output Data
- Output File (```OutputFile.csv```)
    - **Desc**: Filtered Output of a Pandas Dataframe containing the 10% Extreme in terms of Average Half Lives among the Measured YORFs
    - **Format**: Comma-Separated Value (CSV) file
    - **File Location**: Stored within the ```Output``` folder

*Both Input Files and Output Path are Configurable at the start of the script*

## Assignment Description
The script was developed to solve the following tasks:

1. Step 1 goes here...
2. Step 2 goes here...