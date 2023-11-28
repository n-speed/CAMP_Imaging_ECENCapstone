import pandas as pd

def importing():
    '''Imports the data as a dataframe and then tranposes it
    
    NOTE: This is currently separate as it will later take in "n" number of .csv files'''
    cc_data = pd.read_csv('src/data/raw_data/cotton/CC_2023.csv')
    ch_data = pd.read_csv('src/data/raw_data/cotton/CH_2023.csv')
    cv_data = pd.read_csv('src/data/raw_data/cotton/CV_2023.csv')
    exg_data = pd.read_csv('src/data/raw_data/cotton/EXG_2023.csv')

    data_ary = [cc_data,ch_data,cv_data,exg_data]

    return data_ary
