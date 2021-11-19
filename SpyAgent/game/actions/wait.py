from .move import Move


class Wait(Move):

    def __init__(self, spy):
        super().__init__(spy, spy.position)

    def doable(self):
        return super().doable()

    def do(self):
        super().do()

    def to_string(self):
        return "Wait("+str(int(self.pos.x))+";"+str(int(self.pos.y))+")"
