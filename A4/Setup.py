metadata = {
    'Author      ': 'Jay Annadurai',
    'Date        ': '22 Mar 2024',
    'Project     ': 'A4-PSWMPredictor',
    'Version     ': 1.0,
    'Description ': 'Unzips BZ files in preparation for the main script'
}

# Import Libraries for Adjusting the System Path
import sys
import os

# Temporary adjustment to the system path to ensure the JayUtilities module can be imported
script_dir = os.getcwd()  # Gets the directory where the script is located
sys.path.append(script_dir)

# Import DataIO as jio from JayUtilities
from JayUtilities import DataIO as Jio

# Set the input and output folders for jio
Jio.input_folder = 'Source'
Jio.output_folder = 'Input'

# List of files to unzip
files_to_unzip = [
    'E_coli_K12_MG1655.400_50.bz2',
]

# Call the unzip_files method to unzip the specified files
Jio.unzip_files(files_to_unzip)

#%%
