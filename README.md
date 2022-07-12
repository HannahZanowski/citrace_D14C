# citrace_D14C
This repository houses various scripts used to analyze deglacial Pacific D14C in the C-iTRACE simulation as presented in _Zanowski et al. 2022_

Access through Zenodo: <br>
[![DOI](https://zenodo.org/badge/513294554.svg)](https://zenodo.org/badge/latestdoi/513294554)

### Paper citation:
Zanowski, H., A. Jahn, S. Gu, Z. Liu, and T.M. Marchitto, 2022: Decomposition of deglacial Pacific radiocarbon age controls using an isotope-enabled ocean model (_Paleoceanography and Paleoclimatology_)

### Model Information
More information about the C-iTRACE simulation and links to the model output can be found [here](https://sites.google.com/colorado.edu/citrace/home)

### Repository Contents

This repository contains the following files:
1. citrace_env.yml -- the python environment used for this project
2. CiTRACE_Pac_D14C_figures.ipynb -- a jupyter notebook containing the code for the analyses and the figures in Zanowski et al. 2022
3. carbon_isotope_functions.py -- a python script containing various functions to compute radicarbon age. Used in CiTRACE_Pac_D14C_figures.ipynb
4. CiTRACE_Adapted_Region_Mask.nc -- a netCDF file containing the region mask for the C-iTRACE simulation. Used in CiTRACE_Pac_D14C_figures.ipynb
5. citrace_fw.txt -- a text file containing time series of the freshwater forcing applied in the C-iTRACE simulation. Used in CiTRACE_Pac_D14C_figures.ipynb
6. regrid_citrace_D14C.py -- a python script that regrids the C-iTRACE radiocarbon output onto a 1˚x1˚ grid for direct comparison to GLODAPv1 (Key et al., 2004)
