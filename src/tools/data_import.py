import os
import pandas as pd

def data_import(datapath):
    """Simple function for importing data into a Pandas Dataframe
        datapath -- OS datapath to the .csv file
        dataset -- which dataset frame will be populated
    """
    
    df = pd.read_csv(datapath)
    return print(df)


