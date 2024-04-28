# Import Libraries
import os  # File Manipulation
import gzip  # File Compression
import bz2 # Alt File Compression
import shutil  # File Data Transfer
import numpy as np  # Computation
import pandas as pd  # Data Reading

metadata = {
    'Author      ': 'Jay Annadurai',
    'Date        ': '12 Apr 2024',
    'Project     ': 'JayUtilities',
    'Version     ': 1.2,
    'Description ': "Contains Utility Functions as used by Jay Annadurai's Scripts"
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~
#  Data Input/Output Class
# ~~~~~~~~~~~~~~~~~~~~~~~~~


class DataIO:
    # Static variables for input and output folders
    input_folder = 'Input'
    output_folder = 'Output'
    # Supported File Formats
    file_formats = ['txt', 'csv', 'tsv', 'xlsx', 'xls']

    # ~~~~~~~~~~~~~~~~~~~~~ #
    #  File <-> DF Methods  #
    # ~~~~~~~~~~~~~~~~~~~~~ #

    @staticmethod
    def file_to_df(
            file_name: str,
            return_dict: bool = True,
            include_df_shape: bool = True,
            alternate_forms: bool = False,
            force_encode_format: bool | str = False,
            read_args: dict = None  # Dictionary for additional read arguments
    ) -> pd.DataFrame | dict:
        """
        Loads a file from the input directory into a pandas DataFrame and returns a df or dictionary

        :param file_name: The name of the file to be loaded from the input directory.
        :param return_dict: If True, returns a dictionary with file and DataFrame details; else, returns the DataFrame.
        :param include_df_shape: If True, includes the shape and column details of the DataFrame.
        :param alternate_forms: If True, includes alternate forms of the DataFrame such as numeric only or 1D vector.
        :param force_encode_format: Optionally forces the encoding format to read the file as ['csv', 'tsv', 'xlsx']
        :param read_args: Optional dictionary to specify additional arguments for reading the file.

        Optional Read_Args include 'skiprows' to skip rows when parsing the file or 'header=None' to prevent headers

        :return: A dictionary with the file and DataFrame information, or the DataFrame itself.
        """
        if read_args is None:
            read_args = {}

        file_path = os.path.join(DataIO.input_folder, file_name)
        file_name, file_extension = os.path.splitext(file_name)

        # Remove the period from the file extension if it exists
        file_extension = file_extension.lstrip('.')

        # Set the File Extension to Lowercase
        file_extension = file_extension.lower()

        # Set the encoding format based on the file extension unless it has been overrided
        if force_encode_format is False:
            encode_format = file_extension
        else:
            # Assumes a String value for the new encode format is provided
            if force_encode_format.lower() in DataIO.file_formats:
                encode_format = force_encode_format.lower()
            else:
                # Raise Value Error if the Encode Format is Incorrect
                raise ValueError(f"Encode Format {force_encode_format} is Invalid, try: {str(DataIO.file_formats)}")

        # Parse the File based on its extension
        if encode_format in ['xlsx', 'xls']:
            df = pd.read_excel(file_path, **read_args)
        elif encode_format == 'tsv':
            df = pd.read_csv(file_path, sep='\t', **read_args)
        elif encode_format == 'csv':
            df = pd.read_csv(file_path, sep=',', **read_args)
        else:
            if encode_format not in DataIO.file_formats:
                raise TypeError(f"Unsupported file extension. Must be one of {DataIO.file_formats}")

        # Establish all the Relevant Data
        df_dict = {
            "file": {
                "name": file_name,
                "ext": file_extension,
                "path": file_path,
            },
            "df": df
        }

        # If the include_df_shape flag is enabled, add data regarding the shape of the DataFrame
        if include_df_shape:
            max_rows = 100
            metadata = {
                "rows": {
                    "count": df.shape[0],
                    "names": df.index.tolist() if df.shape[0] <= max_rows else f"Exceeds Row Limit of {max_rows}"
                },
                "cols": {
                    "count": df.shape[1],
                    "names": df.columns.tolist(),
                    "dtypes": df.dtypes.to_dict()
                }
            }
            df_dict["metadata"] = metadata

        if alternate_forms:
            numeric_df = df.select_dtypes(include=[float, int])
            df_dict['numeric'] = numeric_df
            df_dict['vector'] = numeric_df.values.flatten()

        if return_dict:
            return df_dict
        else:
            return df

    @staticmethod
    def df_to_file(
            df: pd.DataFrame,
            file_name: str,
            file_format: str,
            keep_header: bool = True,
            keep_index: bool = False,
            save_args: dict = None  # Additional arguments for saving the file
    ) -> None:
        """
        Saves a pandas DataFrame to a file in the output directory in the specified format.

        :param df: The DataFrame to save.
        :param file_name: The name of the file without the extension.
        :param file_format: The format of the file to save ('csv', 'tsv', 'xlsx', 'xls').
        :param keep_header: If True, include the header in the output file; otherwise, no header is written.
        :param keep_index: If True, include the index in the output file; otherwise, no index is written.
        :param save_args: Optional dictionary to specify additional arguments for saving the file.
        :return: None
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("The provided data is not a pandas DataFrame")

        if save_args is None:
            save_args = {}

        # Set the File Format to Lowercase
        file_format = file_format.lower()

        if file_format not in DataIO.file_formats:
            raise ValueError(f"Unsupported file format. Choose from {DataIO.file_formats}")

        file_path = os.path.join(DataIO.output_folder, f"{file_name}.{file_format}")

        # Saving the DataFrame to the file using the specified format
        if file_format in ['xlsx', 'xls']:
            df.to_excel(file_path, index=keep_index, header=keep_header, **save_args)
        elif file_format in ['csv', 'txt']:
            df.to_csv(file_path, index=keep_index, header=keep_header, sep=',', **save_args)
        elif file_format == 'tsv':
            df.to_csv(file_path, index=keep_index, header=keep_header, sep='\t', **save_args)
        else:
            raise ValueError("Unexpected error in saving the file.")

    # ~~~~~~~~~~~~~~~~~~~~~~ #
    #  File <-> Zip Methods  #
    # ~~~~~~~~~~~~~~~~~~~~~~ #

    @staticmethod
    def unzip_files(file_names):
        """
        Unzips the specified .gz or .bz2 files from the input folder to the output folder.
        Accepts either a single file name or a list of file names. Automatically detects
        the file extension and uses the appropriate decompression tool (gzip or bz2).

        :param file_names: A single file name or a list of file names to be unzipped.
        """
        # Check if file_names is a single string, if so convert it to a list
        if isinstance(file_names, str):
            file_names = [file_names]

        # Loop through each file name in the list
        for file_name in file_names:
            # Construct the full path of the source file in the input folder
            source_path = os.path.join(DataIO.input_folder, file_name)
            # Remove the file extension for the output file name
            output_file_name = file_name.rsplit('.', 1)[0]
            # Construct the full path of the output file in the output folder
            output_path = os.path.join(DataIO.output_folder, output_file_name)

            # Determine the appropriate decompression method based on the file extension
            if file_name.endswith('.gz'):
                open_func = gzip.open
            elif file_name.endswith('.bz2'):
                open_func = bz2.open
            else:
                print(f"Unsupported file format for {file_name}")
                continue

            # Open the source file in read-binary ('rb') mode
            with open_func(source_path, 'rb') as input_file:
                # Open the output file in write-binary ('wb') mode
                with open(output_path, 'wb') as output_file:
                    # Copy the content from the input file to the output file
                    shutil.copyfileobj(input_file, output_file)
            # Print the status of the unzipped file
            print(f'Unzipped {file_name} to {output_path}')

    @staticmethod
    def zip_files(file_names, format='gz'):
        """
        Compresses the specified files from the output folder to the input folder in .gz or .bz2 format.
        Accepts either a single file name or a list of file names. The format for compression can be specified
        ('gz' for gzip, 'bz2' for bzip2), defaulting to 'gz'.

        :param file_names: A single file name or a list of file names to be compressed.
        :param format: Compression format ('gz' or 'bz2').
        """
        # Check if file_names is a single string, if so convert it to a list
        if isinstance(file_names, str):
            file_names = [file_names]

        # Loop through each file name in the list
        for file_name in file_names:
            # Construct the full path of the input file in the output folder
            input_path = os.path.join(DataIO.output_folder, file_name)
            # Add the appropriate file extension for the output file name based on the specified format
            output_file_name = f"{file_name}.{format}"
            # Construct the full path of the output file in the input folder
            output_path = os.path.join(DataIO.input_folder, output_file_name)

            # Determine the appropriate compression method based on the format parameter
            if format == 'gz':
                open_func = gzip.open
            elif format == 'bz2':
                open_func = bz2.open
            else:
                print(f"Unsupported compression format for {format}")
                continue

            # Open the input file in read-binary ('rb') mode
            with open(input_path, 'rb') as input_file:
                # Open the output file in write-binary ('wb') mode for compression
                with open_func(output_path, 'wb') as output_file:
                    # Copy the content from the input file to the output file, compressing it in the process
                    shutil.copyfileobj(input_file, output_file)
            # Print the status of the compressed file
            print(f'Compressed {file_name} to {output_path}')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    #  Dataframe Manipulation Methods  #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Static method to print details of a single DataFrame or multiple DataFrames stored in a list or dict
    @staticmethod
    def print_df(
            df: pd.DataFrame | dict | list[pd.DataFrame],
            df_name: str = "DataFrame",
            rows: int = 10,
            show_dtypes: bool = False,
            separator_char: str = '~'
    ) -> None:
        """
        Prints detailed information for a list or dictionary of DataFrames.

        :param df: A single DataFrame, a list of DataFrames, or a dictionary with DataFrame names as keys.
        :param df_name: Name of the DataFrame.
        :param rows: Number of rows to display from each DataFrame.
        :param show_dtypes: Enables the Display of Column Datatypes.
        :param separator_char: Character used to create a separator line.

        :return None: Only Prints the Dataframe Details
        """
        if isinstance(df, list) and not(isinstance(df, dict)):
            print(f"\n")
            for i, df in enumerate(df, 1):
                df_name = f"{df_name} {i}"
                DataIO.print_dataframe_details(df, df_name, rows, show_dtypes, separator_char)
        elif isinstance(df, dict):
            print(f"{df_name}\n")
            for df_name, df in df.items():
                # In case a dictionary of information is fed, look for the dataframe within the dict itself
                if isinstance(df, dict):
                    def find_dataframe(dictionary):
                        for value in dictionary.values():
                            if isinstance(value, pd.DataFrame):
                                return value
                        return None  # Return None if no DataFrame is found

                    # Search for the Dataframe
                    df = find_dataframe(df)

                    # If the dataframe is found
                    if df is None:
                        raise ValueError(f"No DataFrame found within the input Dict {df_name}")

                DataIO.print_dataframe_details(df, df_name, rows, show_dtypes, separator_char)
        elif isinstance(df, pd.DataFrame):
            DataIO.print_dataframe_details(df, df_name, rows, show_dtypes, separator_char)
        else:
            raise TypeError("Input should be a DataFrame, a list of DataFrames, or a dictionary as df_name:df.")

    # Static helper method to print the details of a single DataFrame
    @staticmethod
    def print_dataframe_details(
            df: pd.DataFrame,
            df_name: str = "DataFrame",
            length: int = 10,
            show_dtypes: bool = False,
            separator_char: str = '~'

    ) -> None:
        """
        Prints the details of a single DataFrame including its name, dimensions, column types, and top rows.

        :param df: The DataFrame to print.
        :param df_name: Name of the DataFrame.
        :param length: Number of rows to display from the DataFrame.
        :param show_dtypes: Enables the Display of Column Datatypes.
        :param separator_char: Character used to create a separator line.

        :return None: Only Prints the Dataframe Details
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"The provided data is not a pandas DataFrame: {type(df)}")

        info_str = f"{df_name}: {df.shape[0]} Row x {df.shape[1]} Col"
        separator = separator_char * len(info_str)

        print(separator)
        print(info_str)
        print(separator + '\n')

        if show_dtypes:
            col_types = ', '.join([f"{col}: {dtype}" for col, dtype in df.dtypes.items()])
            print(f"< Col Types > : [ {col_types} ]\n")

        print(df.head(length))
        print(separator + '\n\n')

    @staticmethod
    # Wrapper Method for Pandas Melt with Added Documentation
    def wide_to_long(
            df: pd.DataFrame,
            group_by: str | list[str],
            grouped_columns_name: str,
            dependent_variable_name: str
    ) -> pd.DataFrame:
        """
        Transforms a Wide Format / Tabular DataFrame into a Long Format / Series DataFrame.
        Simply a Wrapper Method for Pandas.melt() for Jay's Readability

        :param df: The wide-format DataFrame to be melted.
        :param group_by: Single column name or list of column names to group per within the long format.
                         For example, in a DataFrame with columns ['population', '0 min', '5 min', '10 min'],
                         you might group by 'population'.
        :param grouped_columns_name: Column name for the column containing the labels for the melted columns.
                         For the example DataFrame, this could be 'time' representing the different time intervals.
        :param dependent_variable_name: Column name of the values of the respective labels of the melted columns.
                         For the example DataFrame, this could be 'pop_count' representing the dependent variable.

        :return: A long-format DataFrame.

        Usage Example:
        DataFrame with columns ['population', '0 min', '5 min', '10 min']
        long_df = DataIO.wide_to_long(
                    wide_df,
                    group_by='population',
                    grouped_columns_name='time',
                    dependent_variable_name='pop_count'
        )
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("The provided data is not a pandas DataFrame")

        # Perform the melt operation
        melted_df = pd.melt(df, id_vars=group_by, var_name=grouped_columns_name, value_name=dependent_variable_name)

        return melted_df

    @staticmethod
    # Personal Function to Process the Values of a Dataframe
    def preprocess_long_df_values(
            long_df: pd.DataFrame,
            data_columns: str | list,
            behavior_nans: str | dict | int | float = 'Keep',
            behavior_negs: str | dict | int | float = 'Keep',
            behavior_zeroes: str | dict | int | float = 'Keep',
            drop_behavior: str = 'Row',
            force_type: str | list | dict | None = None,
            inplace: bool = False,
            reset_index: bool = True
    ) -> pd.DataFrame:
        """
        Preprocesses specified columns of a DataFrame based on selected criteria
        Can handle NaN values, negatives, zeroes, and selected data types

        Parameters:
        :param long_df: (pd.DataFrame) DataFrame to process
        :param data_columns: (str/list) Column name(s) to modify
        :param behavior_nans: (str/dict/value) Handling of NaN values ('Drop', 'Keep', {'Replace': value}, value)
        :param behavior_negs: (str/dict/value) Handling of neg values ('Drop', 'Keep', 'Abs', {'Replace': value}, value)
        :param behavior_zeroes: (str/dict/value) Handling of zero values ('Drop', 'Keep', {'Replace': value}, value)
        :param drop_behavior: (str) Specifies how to drop data ('Row', 'Col', 'Value')
        :param force_type: (type/list/dict) Type(s) to convert specified columns to
        :param inplace: (bool) Default: True, modifies the DataFrame in place; otherwise, returns a modified copy.
        :param reset_index: (bool) Default: True, resets the index prior to finishing
        Returns:
        :return Processed pd.Dataframe with modified columns or None if inplace is false
        """

        # # Check if pandas is imported, and import it if it isn't
        # if 'pd' not in globals():
        #     import pandas as pd
        #
        # # Check if numpy is imported, and import it if it isn't
        # if 'np' not in globals():
        #     import numpy as np

        # Work on a copy if modifications are not to occur in place
        df = long_df if inplace else long_df.copy()

        # Ensure that data_columns is a list for uniform processing.
        if isinstance(data_columns, str):
            data_columns = [data_columns]

        # Capitalize the argument names of the behaviors
        for arg in [behavior_nans, behavior_zeroes, behavior_negs]:
            if arg is str:
                arg.capitalize()

        # Force conversion of column data types if specified.
        # This step ensures that the data in each specified column is of a consistent type, as defined by the user.
        # The type conversion is performed before handling NaN, negative, and zero values to ensure data consistency.
        if isinstance(force_type, dict):
            # If force_type is a dictionary, apply each specified type to the corresponding column.
            for col, dtype in force_type.items():
                if col in long_df.columns:
                    long_df[col] = long_df[col].astype(dtype)
        elif isinstance(force_type, list) and len(force_type) == len(data_columns):
            # If force_type is a list with a length matching data_columns
            # Apply each type in order to the corresponding column
            for col, dtype in zip(data_columns, force_type):
                long_df[col] = long_df[col].astype(dtype)
        elif force_type is not None:
            # If force_type is a single data type, apply it to all specified columns.
            for col in data_columns:
                if col in long_df.columns:
                    long_df[col] = long_df[col].astype(force_type)

        # Helper Function to coordinate the drop behavior
        def drop_values(df, column_name, drop_behavior: str, condition=None):
            """
            Drops rows, columns, or specific values based on the drop behavior.

            Parameters:
            - df: DataFrame being processed.
            - column_name (str): Column name to apply the drop behavior to.
            - drop_behavior (str)_name: Specifies how to drop ('Row', 'Col', or 'Value').
            - condition: Optional condition for dropping specific values. Only used when drop_behavior is 'Value'.
            """

            # Validate the Argument Name; ensure drop_behavior is not plural and is capitalized
            drop_behavior = drop_behavior.rstrip('s').capitalize()

            # Drop Rows, Columns, or Individual Values
            if drop_behavior == 'Row':
                # Drop entire rows where the condition is met (used for NaNs and possibly zeroes/negatives)
                return df.dropna(subset=[column_name]) if condition is None else df[~condition]
            elif drop_behavior == 'Col' or drop_behavior == 'Column':
                # Drop the entire column
                return df.drop(columns=[column_name])
            elif drop_behavior == 'Value' and condition is not None:
                # Only drop specific values that meet the condition (for negatives and zeroes)
                df.loc[condition, column_name] = np.nan
            return df

        # Helper Functions for the Processing of Certain Types of Values:
        def handle_nan_values(df, column_name, behavior, drop_behavior):
            """Handles NaN values in a specified column based on the behavior."""
            if behavior == 'Keep':
                return df
            elif behavior == 'Drop':
                df = drop_values(df, column_name, drop_behavior)
            elif isinstance(behavior, dict) and 'Replace' in behavior:
                df[column_name].fillna(behavior['Replace'], inplace=True)
            elif isinstance(behavior, (int, float, str)):
                df[column_name].fillna(behavior, inplace=True)
            return df

        def handle_negative_values(df, column_name, behavior, drop_behavior):
            """Handles negative values in a specified column based on the behavior."""
            if behavior == 'Keep':
                return df
            elif behavior == 'Drop':
                df = drop_values(df, column_name, drop_behavior, df[column_name] < 0)
            elif behavior == 'Abs':
                df[column_name] = df[column_name].abs()
            elif isinstance(behavior, dict) and 'Replace' in behavior:
                df[column_name] = np.where(df[column_name] < 0, behavior['Replace'], df[column_name])
            elif isinstance(behavior, (int, float, str)):
                df[column_name] = np.where(df[column_name] < 0, behavior, df[column_name])
            return df

        def handle_zero_values(df, column_name, behavior, drop_behavior):
            """Handles zero values in a specified column based on the behavior."""
            if behavior == 'Keep':
                return df
            elif behavior == 'Drop':
                df = drop_values(df, column_name, drop_behavior, df[column_name] == 0)
            elif isinstance(behavior, dict) and 'Replace' in behavior:
                df[column_name] = np.where(df[column_name] == 0, behavior['Replace'], df[column_name])
            elif isinstance(behavior, (int, float, str)):
                df[column_name] = np.where(df[column_name] == 0, behavior, df[column_name])
            return df

        # Process each specified column for NaN, negative, and zero values.
        for col in data_columns:
            if col not in df.columns:
                print(f"Column {col} not found in DataFrame.")
                continue

            # Determine if handling for NaNs and negatives should be delayed if they are to be converted to zeroes
            delay_negatives = ((isinstance(behavior_negs, dict)
                               and 'Replace' in behavior_negs
                               and behavior_negs['Replace'] == 0)
                               and behavior_zeroes != 'Keep')
            delay_nans = ((isinstance(behavior_nans, dict)
                          and 'Replace' in behavior_nans
                          and behavior_nans['Replace'] == 0)
                          and behavior_zeroes != 'Keep')

            # Handle NaN values unless delayed
            if not delay_nans:
                df = handle_nan_values(df, col, behavior_nans, drop_behavior)

            # Conditional processing based on delay decisions
            if delay_negatives:
                # Handle zero values before negatives if delaying negatives
                df = handle_zero_values(df, col, behavior_zeroes, drop_behavior)
                # Now handle negatives since we initially delayed it
                df = handle_negative_values(df, col, behavior_negs, drop_behavior)
            else:
                # Handle negatives first if not delaying
                df = handle_negative_values(df, col, behavior_negs, drop_behavior)
                # Then handle zero values
                df = handle_zero_values(df, col, behavior_zeroes, drop_behavior)

            # Handle NaN values now if they were delayed
            if delay_nans:
                df = handle_nan_values(df, col, behavior_nans, drop_behavior)

        # Reset the Index if Enabled
        if reset_index:
            df.reset_index(drop=True, inplace=True)

        # Return the modified DataFrame if not inplace, otherwise return None
        return df if not inplace else df
#%%
