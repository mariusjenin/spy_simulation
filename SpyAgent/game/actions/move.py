from .action import Action


class Move(Action):

    def __init__(self, spy, pos):
        super().__init__(spy)
        self.pos = pos

    # Return if the move action is doable
    def doable(self):
        # We test if the box is walkable (box crossable and not spotted)
        box_tested = self.spy.current_room.at_pos(self.pos)
        return box_tested.crossable and not box_tested.spotted

    #do the move action
    def do(self):
        self.spy.move(self.pos)

    def to_string(self):
        return "Move("+str(int(self.pos.x))+";"+str(int(self.pos.y))+")"
