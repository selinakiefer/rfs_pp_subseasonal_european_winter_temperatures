# This function extracts a defined time period from a pandas dataframe. The start- and
# end-date of this timeseries are defined as datetime-objects. Then, the time column
# of the dataframe is converted to a datetime-object and the index of the dataframe is
# set to the time. Now, the previously defined time period is extracted from the 
# dataframe using .truncate(). 
from datetime import datetime
import pandas as pd

def truncate_data_by_date(df_data, time_name, start_date, end_date):
    
    start_date = datetime.strptime(start_date, '%Y_%m_%d')
    
    end_date = datetime.strptime(end_date, '%Y_%m_%d')
        
    df_data[time_name]=pd.to_datetime(df_data[time_name])
    
    df_data=df_data.set_index(time_name)
    
    df_data = df_data.sort_index().truncate(before=start_date, after=end_date)
    
    df_data = df_data.reset_index()

    return df_data
