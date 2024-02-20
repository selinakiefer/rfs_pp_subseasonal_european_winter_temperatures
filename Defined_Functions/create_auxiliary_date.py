# For a nice representation of the date at a plot, a "auxiliary date" is created. This is simply a
# timeseries of dates of a leap year winter (here 2003/2004). The year itself does not matter
# since only the month and day are shown on a plot. It is easier to extract the month and day
# from a datetime object than to create it by hand. Therefore the auxiliary date is created. 
# Unfortunately, the mean value of the skill measure are not sorted in the order of a winter
# (Nov-Apr) using groupby() but instead in the chronological order of the month's number
# (Jan-Dec). To order the auxiliary date in the same way, several steps are necessary. At first,
# the months of the winter are determined by grouping the auxiliary time and taking the mean. This
# creates a list of all winter months.
# The dataframe is then sorted by month in ascending order. Therefore, the index is set to the
# time and the dataframe is started to be filled by the data of the first chronological month
# (Jan) of the auxiliary date (loc[]). The data of all other months are then appended to the 
# dataframe.

from datetime import datetime, timedelta
import pandas as pd
import numpy as np

def create_auxiliary_date(start_month_winter, start_day_winter, end_month_winter, end_day_winter):

    start_auxiliary_time = datetime(2003, start_month_winter, start_day_winter)
    end_auxiliary_time = datetime(2004, end_month_winter, end_day_winter)
    days_of_winter = ((end_auxiliary_time-start_auxiliary_time).days)+1
    forecast_dates_winter = [start_auxiliary_time + timedelta(days=x) for x in range(0, days_of_winter)]
    
    df_auxiliary_time = pd.DataFrame(np.arange(0, days_of_winter))
    df_auxiliary_time['auxiliary_date'] = forecast_dates_winter
    df_auxiliary_time = df_auxiliary_time.set_index('auxiliary_date')
    df_months_of_winter = df_auxiliary_time.groupby(df_auxiliary_time.index.month).mean()
    df_months_of_winter = df_months_of_winter.reset_index() 
    months_of_winter = list(df_months_of_winter['auxiliary_date'])
    
    df_auxiliary_time_sorted = df_auxiliary_time.loc[df_auxiliary_time.index.month == months_of_winter[0]]
    for l in range(len(months_of_winter)-1):
        df_auxiliary_time_sorted = df_auxiliary_time_sorted.append(df_auxiliary_time.loc[df_auxiliary_time.index.month == months_of_winter[l+1]])
    df_auxiliary_time_sorted = df_auxiliary_time_sorted.reset_index()
    
    auxiliary_time = df_auxiliary_time_sorted['auxiliary_date']
    
    return auxiliary_time
    
