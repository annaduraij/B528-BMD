**_A1 - Correlation Matrices_**
**_Author: Jay Annadurai_**
**_Date: 14 February 2024_**
**_Programming Language & Version: Python 3.11_**

__Dependencies__
Pandas: For data reading and manipulation.
Seaborn: For advanced data visualization, specifically for generating heatmaps.
Matplotlib: For basic data visualization.
Numpy: For computation.

__Input Data__
Files: Gene expressions quantified in RPKM of microRNAs among various classes of Cancer as Matrices
Format: Tab-Separated Value Files
File Location: Stored within the data folder.
* matrix1.txt
* matrix2.txt

__Output Files:__

Files: Heatmaps of the correlation matrices of the respective input matrices.
Format: PNG images.
Location: Stored within the output folder.

__Usage:__

To use this script, ensure all dependencies are installed and place your .tsv input files in the data folder. Run the script, and it will automatically generate heatmaps for each input file and save them in the output folder. The Pearson correlation coefficients of the correlations are printed to the console.

__Script:__
The python script reads gene expression quantified in RPKM of microRNAs among various classes of Cancer from the 'matrix1' and 'matrix2' data files. It then generates a 12x12 pearson correlation matrix and a coinciding heatmap for each respective file. Finally, it then compares matrix 1 and matrix 2 with each other using a pearson correlation. 