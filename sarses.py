from typing import List, Any
from dataclasses import dataclass, replace, field
import numpy as np

@dataclass
class STATE:
    obs_vector: np.array(dtype = float) # state obsVector
    raw_game_state: Any # raw game_state if needed

@dataclass
class STATE_METRICS:
    pass

@dataclass
class SARS:
    s1: STATE = None # First State
    action: List[str] = field(default_factory=list) # List of choosen actions for unit
    reward: float = None #Reward for transition from s1 to s2
    s2: STATE = None # Second State