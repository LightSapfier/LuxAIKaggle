import math, sys
from lux.game import Game
from lux.game_map import Cell, RESOURCE_TYPES
from lux.constants import Constants
from lux.game_constants import GAME_CONSTANTS
from lux import annotate
from dqn_class import DDQN
from agent_config_class import AGENT_CONFIG 

DIRECTIONS = Constants.DIRECTIONS
game_state = None



default_config = AGENT_CONFIG(
player_agent_name = 'DDQN'
)

player_agent_dict = {
    'DDQN': DDQN
}
def agent(observation, configuration,agent_config = default_config):
    global game_state

    ### Do not edit ###
    if observation["step"] == 0:
        game_state = Game()
        game_state._initialize(observation["updates"])
        game_state._update(observation["updates"][2:])
        game_state.id = observation.player
    else:
        game_state._update(observation["updates"])
    
    player_agent = player_agent_dict[agent_config.player_agent_name]
    actions = []
    return actions