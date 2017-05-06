import flags
from run_manager import RunManager
from character import Character
import level

#################################
flags.run_manager = RunManager()#
flags.character = Character()   #
#################################

level.load_level(flags.run_manager.display_manager.map)
flags.run_manager.start_game()
