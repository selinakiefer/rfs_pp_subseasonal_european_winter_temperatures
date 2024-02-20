# This function applies the cold wave definition of Smid et al. (2019, 
# https://doi.org/10.1016/j.uclim.2018.12.010) to a dataframe. At first, it is checked 
# which temperatures in the dataframe are lower (.le() ) as the given threshold defined 
# by the cold wave definition. These values are set to 'True'. Then, a new column called
# 'labels is created which shows if two neighbouring time points both have 'True' values.
# This is done by comparing the current time point with its following time point
# (.shift() ). In case they are the same, they get the same number starting by 1. In case 
# they are different (!=), the next number (.cumsum() ) is given to the following time
# point. In a next step, it is checked if a at least 3 neighbouring time points have the 
# same number given by (.cumsum() ). This is done by (.value_counts() >=3). If so, in a new
# column called 'flag' a 1 is set, otherwise a 0. In a last step, the days with cold waves are
# determined. If a time point has lower temperatures than the threshold defined by Smid et al.
# (2019) ('cold_wave' == True) and its two following time points also fulfill this criterion
# ('flag' == 1), a 1 is added to a list, otherwise a 0. This list shows then the days with
# cold waves after the definition by Smid et al. (2019). The list is 'sorted', so the original
# time information can be added later.
import pandas as pd

def apply_cold_wave_definition_smid_et_al_2019(df_data_binned, df_data_respective_winter, var_column_name_data, threshold_cold_waves):
    
    list_cold_waves_data = []
    
    df_data_binned['cold_wave'] = df_data_respective_winter[var_column_name_data].le(threshold_cold_waves)
    
    labels = (df_data_binned['cold_wave'] != df_data_binned['cold_wave'].shift()).cumsum()
    df_data_binned['labels'] = labels  
    
    df_data_binned['flag'] = (labels.map(labels.value_counts()) >= 3).astype(int)
    
    for o in range(len(df_data_binned['cold_wave'])):
        cold_waves = 0
        if df_data_binned['cold_wave'][o]==True and df_data_binned['flag'][o]==1:
            cold_waves+=1
        list_cold_waves_data.append(cold_waves) 
        
    return list_cold_waves_data
