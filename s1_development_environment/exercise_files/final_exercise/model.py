from torch import nn

import torch
from tqdm import tqdm
##进度条？
import torch.nn.functional as F



class MyAwesomeModel(nn.Module):
    """My awesome model."""

    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc1 = nn.Linear(256, 128)
        self.fc1 = nn.Linear(128, 64)