import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import optimizer
from torch.utils.data import Dataset,DataLoader

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first = True)
        self.linear = nn.Linear(hidden_size, 20)

    def forward(self, x):
        out, _ = self.lstm(x)
        out = self.linear(out)
        return out
