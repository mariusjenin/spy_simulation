import numpy as np
import os
import time

from .room import Room
from .camera import Camera
from .spy import Spy
from .utils.vec2 import Vec2


class Game:

    def __init__(self):
        self.rooms = []
        self.current = -1

    def init_game(self):
        self.generate_room_1()
        self.generate_room_2()
        self.generate_room_3()

    def run(self):
        self.current = len(self.rooms) - 1
        current_room = self.rooms[self.current]
        self.spy = Spy(current_room)
        current_room.display(self.spy)

        while True:
            self.update()
            self.spy.current_room.display(self.spy)
            if self.spy.spotted:
                break
            else:
                if self.spy.escaped:
                    print("  - Spy escaped floor n°" + str(self.current + 1) + " ! -")
                    if self.current > 0:
                        self.current = self.current - 1
                        self.spy.enter_room(self.rooms[self.current])
                        self.spy.escaped = False
                    else:
                        break
                    time.sleep(2)
                else:
                    time.sleep(0.2)

        if self.spy.spotted:
            print("  - Spy spotted ! -")
        elif self.spy.escaped:
            print("  - Spy escaped the building! -")

    def update(self):
        # Clear console between iteration of the game
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        # Display the Current room with all the cameras and the spy
        self.spy.current_room.compute_spotting()
        self.spy.update_actions()

        action = self.spy.choose()
        action.do()

    def generate_room_1(self):
        # Generate a simple room with only 1 camera and few walls
        room_array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ])

        camera_array = [Camera(Vec2(7, 0), Vec2(0, 1), camera_angle_degree=50, max_tick=6, rotation_degree=75)]

        pos_entrance = Vec2(7, 8)
        room = Room(room_array, pos_entrance, Vec2(1, 1), camera_array)
        self.rooms.insert(0, room)

    def generate_room_2(self):
        # Generate a simple room with only 1 camera and few walls
        room_array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ])

        camera_array = [
            Camera(Vec2(6, 7), Vec2(-1, 0), camera_angle_degree=50, max_tick=11, rotation_degree=120),
            Camera(Vec2(8, 7), Vec2(1, 0), camera_angle_degree=50, max_tick=11, rotation_degree=120),
        ]

        # def __init__(self, pos, direct, max_tick=4, init_tick=0, direct_rotate=1, rotation_degree=90):

        pos_entrance = Vec2(7, 13)
        room = Room(room_array, pos_entrance, Vec2(7, 1), camera_array)
        self.rooms.insert(0, room)

    def generate_room_3(self):
        # Generate a simple room with only 1 camera and few walls
        room_array = np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
                [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ])

        camera_array = [
            Camera(Vec2(14, 0), Vec2(-1, 1), camera_angle_degree=40, max_tick=10, rotation_degree=45),
            Camera(Vec2(19, 5), Vec2(-1, 1), camera_angle_degree=40, max_tick=10, rotation_degree=45)
        ]

        pos_entrance = Vec2(1, 18)
        room = Room(room_array, pos_entrance, Vec2(18, 1), camera_array)
        self.rooms.insert(0, room)
