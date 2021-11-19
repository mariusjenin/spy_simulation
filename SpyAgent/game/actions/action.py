from abc import *


class Action(ABC):

	@abstractmethod
	def __init__(self, spy):
		self.spy = spy

	@abstractmethod
	def doable(self):
		pass

	@abstractmethod
	def do(self):
		pass

	@abstractmethod
	def to_string(self):
		pass
