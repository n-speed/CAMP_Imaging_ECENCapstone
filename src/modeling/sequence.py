import numpy as np
import torch

def train_sequence(train_data):
    seq_length = 1 # looking at previous week's projection
    x_train, y_train = [] , []
    for i in range(len(train_data)-seq_length):
        x_train.append(train_data[i:i+seq_length])
        y_train.append(train_data[i+1:i+seq_length+1])
    x_train, y_train = np.array(x_train), np.array(y_train)
    
    x_train = torch.tensor(x_train, dtype = torch.float32)
    y_train = torch.tensor(y_train, dtype = torch.float32)
    # print(x_train.shape,y_train.shape)

    return x_train, y_train
    # return print(x_train.shape,y_train.shape)


def test_sequence(test_data):
    seq_length = 1
    x_test, y_test = [],[]
    for i in range(len(test_data)-seq_length):
        x_test.append(test_data[i:i+seq_length])
        y_test.append(test_data[i+1:i+seq_length+1])
    x_test, y_test = np.array(x_test), np.array(y_test)

    x_test = torch.tensor(x_test, dtype = torch.float32)
    y_test = torch.tensor(y_test, dtype = torch.float32)
    #print(x_test.shape,y_test.shape)

    return x_test, y_test

    # print(x_test.shape,y_test.shape)