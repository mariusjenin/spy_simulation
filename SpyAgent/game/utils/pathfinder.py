from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


class Pathfinder:

    def __init__(self, room_array_number,spy_pos,pos_exit):
        self.grid = Grid(matrix=room_array_number)
        self.start = self.grid.node(int(spy_pos.x), int(spy_pos.y))
        self.end = self.grid.node(int(pos_exit.x), int(pos_exit.y))
        self.path = []

    def find_path(self):
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

        # Now you can run find_path.
        self.path, runs = finder.find_path(self.start, self.end, self.grid)
        return self.path

    def display_path(self):
        print(self.grid.grid_str(path=self.path, start=self.start, end=self.end))
        print(self.path)

### OLD PATHFINDER BY BEN

    # def add_edge(self, adjacency_list, vertex1, vertex2):
    #
    #     adjacency_list[vertex1].append(vertex2)
    #     adjacency_list[vertex2].append(vertex1)
    #
    # def breadth_first_search(self, adjacency_list, vertex_src, vertex_dest, n_vertices, precedency_list, distance_list):
    #
    #     queue = []
    #
    #     visited_list = [False for i in range(n_vertices)]
    #
    #     for i in range(n_vertices):
    #         distance_list[i] = float('inf')
    #         precedency_list[i] = -1
    #
    #     visited_list[int(vertex_src)] = True
    #     distance_list[int(vertex_src)] = 0
    #     queue.append(vertex_src)
    #
    #     while len(queue) != 0:
    #
    #         current_vertex = queue[0]
    #         queue.pop(0)
    #
    #         for i in range(len(adjacency_list[int(current_vertex)])):
    #
    #             if visited_list[adjacency_list[int(current_vertex)][i]] == False:
    #
    #                 visited_list[adjacency_list[int(current_vertex)][i]] = True
    #                 distance_list[adjacency_list[int(current_vertex)][i]] = distance_list[int(current_vertex)] + 1
    #                 precedency_list[adjacency_list[int(current_vertex)][i]] = current_vertex
    #
    #                 queue.append(adjacency_list[int(current_vertex)][i])
    #
    #                 if adjacency_list[int(current_vertex)][i] == vertex_dest:
    #                     return True
    #
    #     return False
    #
    # def shortest_path(self, room):
    #
    #     n_rows = 10
    #     n_columns = 10
    #     n_vertices = 100
    #     vertex_src = room.pos_entrance.x + room.pos_entrance.y * n_rows
    #     vertex_dest = room.pos_exit.x + room.pos_exit.y * n_rows
    #
    #     adjacency_list = [[] for i in range(n_vertices)]
    #     precedency_list = [0 for i in range(n_vertices)]
    #     distance_list = [float('inf') for i in range(n_vertices)]
    #
    #     path = []
    #     step = vertex_dest
    #
    #     # Remplissage de la liste d'adjacence
    #     for i in range(n_columns):
    #
    #         for j in range(n_rows):
    #
    #             if room.rooms_boxes[i][j].crossable:
    #
    #                 # Case à gauche
    #                 if (i - 1 >= 0) and room.rooms_boxes[i - 1][j].crossable:
    #                     self.add_edge(adjacency_list, i + j, i - 1 + j * n_rows)
    #
    #                 # Case à droite
    #                 if (i + 1 < n_columns) and room.rooms_boxes[i + 1][j].crossable:
    #                     self.add_edge(adjacency_list, i + j, i + 1 + j * n_rows)
    #
    #                 # Case au dessus
    #                 if (j - 1 >= 0) and room.rooms_boxes[j - 1][j].crossable:
    #                     self.add_edge(adjacency_list, i + j, i + j * n_rows - 1)
    #
    #                 # Case en dessous
    #                 if (j + 1 < n_rows) and room.rooms_boxes[j + 1][j].crossable:
    #                     self.add_edge(adjacency_list, i + j, i + j * n_rows + 1)
    #
    #     # Calcul du plus court chemin
    #     self.breadth_first_search(adjacency_list, vertex_src, vertex_dest, n_vertices, precedency_list, distance_list)
    #
    #     # Vectorisation du chemin
    #     path.append(step)
    #
    #     # while precedency_list[step] == -1:
    #     #     path.append(precedency_list[step])
    #     #     step = precedency_list[step]
    #
    #     ##########
    #     for i in range(len(precedency_list)):
    #         if precedency_list[i] > 0:
    #             print(precedency_list[i])
    #
    #     # for i in range(len(adjacency_list)):
    #     # print(adjacency_list[i])
    #
    #     # for i in range(len(distance_list)):
    #     #         print(distance_list[i])
    #
    #     # for i in range(len(path)):
    #     #     if path[i] > 0:
    #     #         print(path[i])
    #     ##########
    #     return path
