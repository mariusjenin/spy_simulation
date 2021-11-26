import numpy as np
from termcolor import colored, cprint

from game.ground import Ground
from game.utils.vec2 import Vec2
from game.wall import Wall


class Room:

    def __init__(self, room_array_number, pent, pex, cams):
        self.room_array_number = room_array_number

        size_x = len(room_array_number)
        size_y = len(room_array_number[0])
        self.room_boxes = np.array([[Ground(Vec2(0, 0)) for i in range(size_x)] for i in range(size_y)])

        # Generate the room boxes
        for i in range(size_x):
            for j in range(size_y):
                if room_array_number[i][j] == 1:
                    self.room_boxes[j][i] = Ground(Vec2(j, i))

                elif room_array_number[i][j] == 0:
                    self.room_boxes[j][i] = Wall(Vec2(j, i))

        self.pos_entrance = pent
        self.pos_exit = pex
        self.cameras = cams

    def display(self, spy):
        char_sep = ''
        char_space = " "
        char_wall = " "
        char_exit = " "
        char_spy = "S"
        color_spotted = 'on_red'
        color_not_spotted = 'on_white'
        color_entrance_exit = "on_green"
        color_spy = "grey"
        color_spy_on_spotted = 'on_red'
        color_spy_on_not_spotted = 'on_blue'
        for j in range(0,len(self.room_boxes)):
            for i in range(0,len(self.room_boxes[j])):
                if self.room_boxes[i][j].crossable:
                    # GROUND
                    if self.room_boxes[i][j].spotted:
                        on_color = color_spotted
                        color_on_spy = color_spy_on_spotted
                    else:
                        if Vec2.equals(self.pos_exit, Vec2(i, j)) or Vec2.equals(self.pos_entrance, Vec2(i, j)):
                            # EXIT |START
                            on_color = color_entrance_exit
                        else:
                            on_color = color_not_spotted
                        color_on_spy = color_spy_on_not_spotted
                    if Vec2.equals(spy.position, Vec2(i, j)):
                        # PLAYER
                        print(
                            char_sep + colored(char_space + char_spy + char_space, color_spy, color_on_spy, attrs=['bold']),
                            end='')
                    else:
                        print(char_sep + colored(char_space + char_exit + char_space, 'white', on_color), end='')

                else:
                    # CAMERA | WALL
                    done = False
                    for k in range(len(self.cameras)):
                        if Vec2.equals(self.cameras[k].position, Vec2(i, j)):
                            # CAMERA
                            print(char_sep + colored(char_wall + "C" + char_wall, 'red', 'on_grey', attrs=['bold']),
                                  end='')
                            done = True
                            break
                    # WALL
                    if not done:
                        print(
                            char_sep + colored(char_wall + char_wall + char_wall, 'white', 'on_grey', attrs=['bold']),
                            end='')
            print(char_sep)

    def at_indices(self, i, j):
        return self.room_boxes[i][j]

    def at_pos(self, pos):
        return self.room_boxes[int(pos.x)][int(pos.y)]

    def get_room_array_number(self):
        size_x = len(self.room_boxes)
        size_y = len(self.room_boxes[0])
        room_array_number_with_cameras = np.array([[0 for i in range(size_x)] for i in range(size_y)])
        for i in range(size_x):
            for j in range(size_y):
                box = self.room_boxes[i][j]
                if not box.spotted and box.crossable:
                    room_array_number_with_cameras[j][i] = 1
                else:
                    room_array_number_with_cameras[j][i] = 0
        return room_array_number_with_cameras

    def compute_spotting(self):
        self.reset_spotting()
        for cam in self.cameras:
            cam.generate_spotting(self)
        pass

    def reset_spotting(self):
        size_x = len(self.room_boxes)
        size_y = len(self.room_boxes[0])
        for i in range(size_x):
            for j in range(size_y):
                self.room_boxes[i][j].spotted = False
