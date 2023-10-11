import torch
import torch.nn as nn
import os

class StandardLSTM(nn.LSTM):
    def __init__(self,input_dim, hidden_dim):
    