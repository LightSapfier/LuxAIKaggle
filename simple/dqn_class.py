# for kaggle-environments
from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES, Position
from lux.game_objects import Unit
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate

DIRECTIONS = Constants.DIRECTIONS
game_state = None

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
import math
import random
import numpy as np

from agent_config_class import AGENT_CONFIG 
class UnitNetwork(nn.Module):
    pass
class CityNetwork(nn.Module):
    pass
class DDQN(nn.Module):
    def __init__(self, config:AGENT_CONFIG):
        pass
    
