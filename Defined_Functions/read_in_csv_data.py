# This function reads in csv-data with pandas and saves it as a pandas dataframe.
import pandas as pd

def read_in_csv_data (PATH_data, ifile_data):
    df_input_data = pd.read_csv(PATH_data+ifile_data)
    #df_input_data = pd.read_csv(PATH_data+ifile_data, index_col=0) # index_col needs to be left out when n_rows>1 000 000 (bug in pandas)
    df_input_data = df_input_data.reset_index()
    return df_input_data 
