import csv
import temp_test
from itertools import count

class node :
	""" Creates an initialized random instance of the input class. csv writing capabilities"""

	# x coord
	x = 0.

	# y coord
	y = 0.

	# z coord
	z = 0.

	# time interval (in 100ths of seconds)
	t = 0

	# unique id to each input
	id = 0 

	# take in info from input class (temp for testing)
	tt = TempTest()

	def x_set (self) :
		self.x = tt.x

	def y_set (self) :
		self.y = tt.y

	def z_set (self) :
		self.z = tt.z

	def t_set (self) :
		self.t = tt.t 


