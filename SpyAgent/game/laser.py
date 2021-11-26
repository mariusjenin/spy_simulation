import numpy as np
import math

from game.utils.vec2 import Vec2
from .detector import Detector


class Laser(Detector):

    def __init__(self, pos, direct, max_tick=4, init_tick=0, direct_rotate=1, rotation_degree=90):
        super().__init__(pos, direct, max_tick, init_tick, direct_rotate, rotation_degree)


    def is_in_bound(self, v, room_max_v):
        return 0<=v.x<=room_max_v and 0<=v.y<=room_max_v

    def generate_spotting(self, room):
        # increment (or decrement if direct_rotate is negative) the tick
        self.tick = self.tick + self.direct_rotate
        # Rotation of the direction vector with the angle β
        # x2 = cosβx1 − sinβy1
        # y2 = sinβx1 + cosβy1

        angle = self.direct_rotate*(self.rotation_rad/(2*self.max_tick+1))
        self.direction = Vec2(
            math.cos(angle) * self.direction.x - math.sin(angle) * self.direction.y,
            math.sin(angle) * self.direction.x + math.cos(angle) * self.direction.y,
        )

        # if the tick is at the end or at the beginning of the rotation we change the direction of the rotation
        if self.tick == self.min_tick or self.tick == self.max_tick:
            self.direct_rotate = self.direct_rotate * -1


        vect = self.direction.normalize()
        room_size = len(room.room_boxes[0])


        # Apply rotation to get current vector
        current_vect = self.direction

        current_cell = self.position + current_vect
        in_sight = room.at_indices(int(np.round(current_cell.x)), int(np.round(current_cell.y))).crossable

        # Compute spotted boxes 
        # print("path for vect ", current_vect)

        while in_sight and self.is_in_bound(current_cell, room_size):
            round_x = int(np.round(current_cell.x))
            round_y = int(np.round(current_cell.y))


            dist_origin_current = (Vec2(round_x, round_y) - self.position).length()
            cell_data = self.get_start_stop(Vec2(round_x, round_y))

            start = cell_data[1]
            stop = cell_data[2]

            if not cell_data[0]:    # not aligned
                x = np.linspace(start.x, stop.x, int(dist_origin_current) + 1)
                y = np.interp(x, (start.x, stop.x), (start.y, stop.y))
                
            else:
                # if cells are on same line/col no need to interpolate
                x = np.linspace(start.x, stop.x, int(dist_origin_current) + 1)
                y = [i for i in range(int(dist_origin_current) + 1)]

            path = [(np.round(x[i]), np.round(y[i])) for i in range(len(x))]
            # path = [(x[i], y[i]) for i in range(len(x))]

            if path.index((self.position.x, self.position.y)) == len(path) - 1:
                path.reverse()

            index = 1
            in_sight = True
            
            while in_sight and index < len(path):
                i = int(path[index][0])
                j = int(path[index][1])

                # print((cell.x, cell.y) in legal_cells, "ezrez")
                if not room.at_indices(i, j).crossable:
                    in_sight = False
                else:
                    room.at_indices(i, j).spotted = True

                index += 1

            current_cell += current_vect
                    



