# This function takes in 3 3D position vectors and gives the angle made between them
#
#

import numpy as np 
import math 

class Angle3D :

	def angle_calc (self, A, B, C) :

		'vectors'
		vector_BA = np.subtract(A, B)
		vector_BC = np.subtract(C, B)
		zero_vector = np.array((0., 0., 0.))

		'distance'
		dist_BA = np.linalg.norm(vector_BA-zero_vector)
		dist_BC = np.linalg.norm(vector_BC-zero_vector)

		'dot product'
		dot_vect = np.dot(vector_BA, vector_BC)

		'combine'
		return math.acos((dot_vect)/(dist_BA * dist_BC))



