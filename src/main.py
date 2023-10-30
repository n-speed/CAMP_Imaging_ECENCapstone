import os

#import modeling.VI_Model
from tools.data_import import data_import

#data_path = os.chdir("src/tools/raw_data/2023_Sample_Data")

data_path = "tools/raw_data/2023_Sample_Data/cotton/EXG_2023.csv"

data_import(data_path)
