from .utils.vec2 import Vec2
from .actions.move import Move
from .actions.wait import Wait
from .utils.pathfinder import Pathfinder


class Spy:

    # Constructeur de Spy
    def __init__(self, room):
        self.enter_room(room)
        self.spotted = False
        self.escaped = False
        self.actions = []

    # Permet de déplacer l'espion à pos
    def move(self, pos):
        self.position = pos
        self.spotted = self.current_room.at_pos(pos).spotted
        if Vec2.equals(pos, self.current_room.pos_exit):
            self.escaped = True

    def enter_room(self, room):
        self.position = room.pos_entrance
        self.current_room = room

    def update_actions(self):
        # We take the shortest path taking into consideration cameras
        pathfinder = Pathfinder(self.current_room.get_room_array_number(), self.position, self.current_room.pos_exit)
        path = pathfinder.find_path()
        # If the path can't be completed we take the path without taking into consideration cameras
        if len(path) == 0:
            pathfinder = Pathfinder(self.current_room.room_array_number, self.position, self.current_room.pos_exit)
            path = pathfinder.find_path()

        self.actions = []
        # The first action is to go towards the exit (pathfinder)
        self.actions.append(Move(self, Vec2(path[1][0], path[1][1])))
        # The second action is to wait at the actual position
        self.actions.append(Wait(self))

        # We now had
        if 0 < int(self.position.y) < len(self.current_room.room_boxes[0]) - 2:
            if 0 < int(self.position.x + 1) < len(self.current_room.room_boxes) - 2:
                self.actions.append(
                    Move(self, self.current_room.at_indices(int(self.position.x + 1), int(self.position.y)).pos))
            if 0 < int(self.position.x - 1) < len(self.current_room.room_boxes) - 2:
                self.actions.append(
                    Move(self, self.current_room.at_indices(int(self.position.x - 1), int(self.position.y)).pos))

        if 0 < int(self.position.x) < len(self.current_room.room_boxes) - 2:
            if 0 < int(self.position.y + 1) < len(self.current_room.room_boxes[0]) - 2:
                self.actions.append(
                    Move(self, self.current_room.at_indices(int(self.position.x), int(self.position.y + 1)).pos))
            if 0 < int(self.position.y - 1) < len(self.current_room.room_boxes[0]) - 2:
                self.actions.append(
                    Move(self, self.current_room.at_indices(int(self.position.x), int(self.position.y - 1)).pos))

    def choose(self):
        # will check every actions set in the order and will do the first doable
        for i in range(len(self.actions)):
            if self.actions[i].doable():
                return self.actions[i]

        # if no action has been done the spy wait to be spotted at his actual position
        return Wait(self)
