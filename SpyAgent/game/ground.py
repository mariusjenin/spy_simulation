from .box import Box


class Ground(Box):

    def __init__(self, pos):
        super().__init__(pos, True)
