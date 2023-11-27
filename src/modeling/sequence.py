import numpy as np
import torch

def train_sequence(train_data):
    temp_ary = train_data[0]
    seq_length = 2 # looking at previous week's projection
    x_train, y_train = [] , [] # training just the cc data for now
    print(len(temp_ary))
    for i in range(len(temp_ary)-seq_length):
        x_train.append(temp_ary[i:i+seq_length])
        y_train.append(temp_ary[i+1:i+seq_length+1])
    x_train, y_train = np.array(x_train), np.array(y_train)
    
    x_train = torch.tensor(x_train, dtype = torch.float32)
    y_train = torch.tensor(y_train, dtype = torch.float32)
    
    return x_train, y_train
    # return print(x_train.shape,y_train.shape)


def test_sequence(test_data):
    temp_ary = test_data[0]
    seq_length = 1
    x_test, y_test = [],[] # testing just the cc test data for now
    for i in range(len(temp_ary)-seq_length):
        x_test.append(temp_ary[i:i+seq_length])
        y_test.append(temp_ary[i+1:i+seq_length+1])
    x_test, y_test = np.array(x_test), np.array(y_test)

    x_test = torch.tensor(x_test, dtype = torch.float32)
    y_test = torch.tensor(y_test, dtype = torch.float32)

    return x_test, y_test

    # print(x_test.shape,y_test.shape)