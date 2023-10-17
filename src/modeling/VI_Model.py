import torch
import torch.nn as nn
import os

class StandardLSTM(nn.LSTM):
    def __init__(self,input_dim, hidden_dim):
        super(StandardLSTM, self).__init__()
        self.linear1 = nn.Linear()
    