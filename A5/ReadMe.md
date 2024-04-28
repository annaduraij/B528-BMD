# A5 - Protein-Protein Interaction Networks

## Script Information

- **Author**: Jay Annadurai
- **Date**: 27 Apr 2024
- **Programming Language & Version**: Python 3.11
- **Project Version**: 1.0

## Description

The JA-A5 PPI Network analysis script performs analytics on an existing protein-protein interaction (PPI) network.
It is also capable of generating a basic PPI in 

## Script Tasks
The A5-PPIN-Analyzer script was developed to solve the following tasks:
1) Import pre-existing protein-protein interaction links as a network with edges and nodes
2) Create an algorithm to compute, within a network, the degree of each node as the number of edges per node
3) Create an algorithm to compute, within a network, the local clustering coefficient of each node
4) Create an algorithm to compute the clustering coefficient of the network from the local clustering coefficients
5) Plot the degrees of network as a distribution and attempt to fit to a powerlaw to test for scale-free structure
6) Per protein list, create a subnetwork using the information from the main Human PPI network
7) Create an algorithm to compute the shortest path between the pairs of nodes
8) Compare the distributions of path lengths between the two lists with a Wilcox test

<hr>

## Unique Dependencies
- **```NetworkX```**: For Network Analysis Tools (Not used for first half of analysis)

## Common Core Dependencies
- **```Pandas```**: For data reading and manipulation.
- **```Numpy```** & **```Scipy```**: For numerical computations and statistical methods.
- **```Matplotlib```** & **```Seaborn```**: For generating data visualizations.
- **```JayUtilities```**: Contains Utility Functions utilized within the script [In Directory as ```JayUtilities.py```]

## Utility Dependencies
- **```os```**: File Manipulation
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
conda create --name JA5-PPIAnalysis python=3.11 pandas numpy scipy seaborn matplotlib networkx
conda activate JA5-PPIAnalysis
```

The Jupyter notebook ```A4-PPIN-Analyzer.ipynb``` contains the script to perform the PPI network analytics.
It also reveals data at the various stages of processing to provide insight into the methodology of the analysis.

<hr>

## Input Data:
- Input Files:
    - ```Human-PPI.txt```
    - ```protein-list1.txt```
    - ```protein-list2.txt```
- **Desc**: Protein-Protein Network Interaction files and protein lists
- **Format**: Tab-Separated Value (TSV) files
- **File Location**: Stored within the ```Input``` folder

## Output Data:
- **Output Files**:
  - ```N/A```
- **Desc**: No output files were generated in the analysis; all output is within the notebook
- **Format**: N/A
- **File Location**: Normally stored within the ```Output``` folder



*Both Input Files and Output Path are Configurable at the start of the script*

<hr>

<br><br>

### Original Assignment:
Write a script which can calculate the degree and clustering coefficient for every node (protein)
in the human protein interaction network (attached). Now calculate the average clustering coefficient
of the network. Finally, test whether the network has a scale-free structure by plotting the degree distribution?

Now write another script which can calculate the shortest path lengths between every pair of nodes (proteins)
in the attached files (two files are attached). Compare the path length distributions between the two protein
sets using a wilcox test. 