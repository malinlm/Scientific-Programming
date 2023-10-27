# Scientific-Programming
### H1N1 vaccines and seasonal flu vaccines project
The project aims to build classifiers for target h1n1 (Vaccines_project.ipynb) and target seasonal (Vaccines_seasonal.ipynp). <br>
Precision-recall curves and most important features can be compared by looking at the outputs of jupyter notebooks. <br>
The data used from (https://www.cdc.gov/nchs/nis/data_files_h1n1.htm) is in H1N1_Flu_Vaccines.csv (35 features, 2 target classes: h1n1 and seasonal). <br>
Functions that were used in the jupyter notebooks are included in helper_functions.py. <br>
PCA visualization that don't show in jupyter notebooks are included in the folder.

## Aims
Aim-1: training and testing different classifiers to determine feature importances for determining whether a participant received h1n1 or seasonal vaccine. <br>
Aim-2: determining the effect of imbalanced data by comparing performance of h1n1 and seasonal classifiers.

## Main results
Most classifiers had features specific to target class as most important features. Imbalanced data of h1n1 (79% = 0) cause poorer precision-recall curves compared to seasonal vaccine classifiers.
