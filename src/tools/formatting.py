# import data_import as di
from sklearn.preprocessing import MinMaxScaler
import math
import pandas as pd

def formatting(raw_data, split_factor):
    cc_train, ch_train, cv_train, exg_train = [],[],[],[]
    cc_test, ch_test, cv_test, exg_test = [],[],[],[]
    # converts the raw data into a list of arrays
    train_data = [cc_train, ch_train, cv_train, exg_train]
    test_data = [cc_test, ch_test, cv_test, exg_test]

    # cuts the column listing the index ids (since they're already in order)
    # transposes each array to format a little nicer with pytorch
    # TODO Currently trimming the dates. Check later to see if problematic
    cc_data = raw_data[0].iloc[1:,1:].T
    ch_data = raw_data[1].iloc[1:,1:].T
    cv_data = raw_data[2].iloc[1:,1:].T
    exg_data = raw_data[3].iloc[1:,1:].T
    data_list = [cc_data,ch_data,cv_data,exg_data]

    # splitting the data into training and test datasets
    # NOTE TODO: Check to see if leaving the dates column in the data set matters
    train_len = math.ceil(len(cc_data) * split_factor) # we pick one of the arrays as they are all the same length
    scale = MinMaxScaler(feature_range = (0,1))
    
    for i, df in enumerate(data_list):
        train_data[i]= data_list[i].iloc[:train_len][:] # the respective data from the 'list' array is split using iloc[][]
        train_data[i] = scale.fit_transform(train_data[i])

        test_data[i]= data_list[i].iloc[train_len:][:]
        test_data[i] = scale.fit_transform(test_data[i])
    # print(train_data[0]) # debug vars
    # print(train_data[1].shape)
    
    return train_data, test_data



# data = di.importing()
# formatting(data,0.75)
