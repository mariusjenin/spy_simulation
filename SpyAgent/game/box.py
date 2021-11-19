from abc import *


class Box(ABC):

    @abstractmethod
    def __init__(self, pos, cr):
        self.pos = pos
        self.crossable = cr
        self.spotted = False
