# This function reads in netcdf-data with xarray and saves the data in a pandas dataframe.
# There are various options for xr.open_dataset: read in grib-data, mask or scale values, replace missing values, decode timestamps, ....
import xarray as xr
import pandas as pd

def read_in_netcdf_data (PATH_data, ifile_data):
	input_data = xr.open_dataset(PATH_data+ifile_data)
	df_input_data = input_data.to_dataframe()
	df_input_data = df_input_data.reset_index()
	return df_input_data
