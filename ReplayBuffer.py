import numpy as np
import torch
from sarses import *

class ReplayBuffer:
    def __init__(self,size: int, default_device = 'cpu'):
        """
        Create Replay Buffer.
        Parameters
        ----------
        size: Max number of SARS'es to keep in the buffer for training phase
        When buffer is overflower, old memories are dropped
        
        """
        self._storage = []
        self._maxsize = size
        self.default_device = default_device
    def __len__(self):
        return len(self._storage)
    
    def add(self, sars: SARS):
        """
        Adds state - action - reward - state (SARS) to buffer.
        Ignores all other attributes of SARS dataclass
        Added attributes are encode/transformed to torch tensors and moved to default_device
        """
        # Add should be rather fast func,
        pass
    def sample(self, batch_size: int) -> torch.FloatTensor():

        pass
        batch.to(self.default_device)
        return batch
