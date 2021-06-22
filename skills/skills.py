# The skill class
# Base class for all game skills

class Skill():
    EXP_MULTIPLIER = 0.42

    def __init__(self, player):
        self._player = player
        self._level = 1
        self._current_exp = 0
        self._total_exp = 0
        self._next_level = 10
