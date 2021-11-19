from .box import Box


class Wall(Box):

    def __init__(self, pos):
        super().__init__(pos, False)
