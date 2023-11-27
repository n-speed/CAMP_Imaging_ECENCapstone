import data_import as di
import numpy as np
import pandas as pd

def formatting(raw_data):
    # cuts the column listing the index ids (since they're already in order)
    # transposes each array to format a little nicer with pytorch
    # NOTE First column is *ALWAYS* the dates
    cc_data = raw_data[0].iloc[:,1:].T
    ch_data = raw_data[1].iloc[:,1:].T
    cv_data = raw_data[2].iloc[:,1:].T
    exg_data = raw_data[3].iloc[:,1:].T



data = di.data_import()
formatting(data)
