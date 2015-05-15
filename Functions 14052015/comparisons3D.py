import numpy as np 
import scipy.stats as sp
import math

class Comparisons :

	# basic comparison. through experimentation/historical data
	# can define a threshold above which motion range is deemed abnormal
	# data_b is expected data_a is observed

	def euc_comp (self, data_a, data_b) :

		return np.linalg.norm(data_a - data_b) 

	def chi_squared (self, data_a, data_b) :

		'flatten the datastructures for looping'
		observed_raw = data_a.tolist()
		expected_raw = data_b.tolist()

		'get n'
		n = len(observed_raw)

		chi_result = sp.chisquare(observed_raw, f_exp=expected_raw)

		chi_value = chi_result[0]

		p_value = chi_result[1]

		return p_value

	def p_val_interp (self, p_in, cutoff) :

		'test if p value given is below the threshold'
		if (1 - p_in) < cutoff :
			return True
		else :
			return False



