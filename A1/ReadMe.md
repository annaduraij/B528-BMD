**_Title:_ A1 - Correlation Matrices**

**_Author:_ Jay Annadurai**

**_Date:_ 22 Jan 2024**


<ins>**Python 3.11 - Conda**</ins>

_Dependencies:_
* pandas
* seaborn
* matplotlib.pyplot

_Input:_
* matrix1.txt
* matrix2.txt

Script:

The python script reads gene expression quantified in RPKM of microRNAs among various classes of Cancer from the 'matrix1' and 'matrix2' data files. It then generates a 12x12 pearson correlation matrix and a coinciding heatmap for each respective file. Finally, it then compares matrix 1 and matrix 2 with each other using a pearson correlation. 