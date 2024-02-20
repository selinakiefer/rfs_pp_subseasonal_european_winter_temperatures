# Random Forests’ Postprocessing Capability of Enhancing Predictive Skill on Subseasonal Timescales - a Flow-Depended View on Central European Winter Weather

This repository provides Python-Code accompanying the paper "Random Forests’ Postprocessing Capability of Enhancing Predictive Skill on Subseasonal Timescales - a Flow-Depended View on Central European Winter Weather".


### Aim of the paper
Comparison of Random Forest based postprocessing models with ECMWF's S2S reforecasts for forecasts of continuous timeseries of 2-meter temperature for Central Europe in the extended winter season (Nov - Apr) and forecasts of the binary occurrence of cold wave days in the same region and time period

### Used methods
Climatological ensemble, S2S Reforecast Ensemble, Quantile Random Forests, Random Forest Classifiers, Impurity based Feature Importance

### Used data
ERA-5 reanalysis data (https://cds.climate.copernicus.eu/cdsapp#!/search?type=dataset&text=ERA5),
E-OBS observational data (https://www.ecad.eu/download/ensembles/download.php), 
ECMWF's S2S reforecast data (https://apps.ecmwf.int/datasets/data/s2s-reforecasts-instantaneous-accum-ecmf/levtype=sfc/type=cf/)

### Necessary Python packages
see "DEPENDENCIES"

### Code structure
see "Overview_Code_Structure.pdf"

For most of the Python scripts, there is a YAML configuration file which needs to be edited before running the Python script. This is indicated in the respective Python files.

