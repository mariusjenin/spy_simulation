from abc import *
import math

class Detector(ABC):

	def __init__(self, pos, direct, max_tick=4, init_tick=0, direct_rotate=1, rotation_degree=90):
		self.position = pos
		self.direction = direct  # Vector which indicates movement direction (x, y)

		self.min_tick = -1 * max_tick
		self.max_tick = max_tick
		self.tick = init_tick  # TODO à revoir car nefonctionne pas avec init_tick != 0
		self.direct_rotate = direct_rotate
		self.rotation_rad = rotation_degree * math.pi / 180

	@abstractmethod
	def generate_spotting(self, room):
		pass

	def get_start_stop(self, cell):
	    aligned = False

	    if self.position.x < cell.x:
	        start = self.position
	        stop = cell
	    elif self.position.x == cell.x:
	        aligned = True

	        if self.position.y < cell.y:
	            start = self.position
	            stop = cell
	        else:
	            start = cell
	            stop = self.position
	    else:
	        start = cell
	        stop = self.position

	    return [aligned, start, stop]