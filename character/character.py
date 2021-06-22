# The character class
# Base class for all player characters

class Character():

    def __init__(self, name):
        self._name = name
        self.skills = []
    


    def get_name(self):
        return self._name
    


    def get_skills(self):
        return self.skills[]