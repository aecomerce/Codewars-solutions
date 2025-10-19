import random
class Ghost(object):
    @property
    def color(self):
        lst_colors = ['white', 'purple', 'yellow', 'red']
        return random.choice(lst_colors)
