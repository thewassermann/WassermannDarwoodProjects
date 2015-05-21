import csv
import numpy as np 

class CsvToVector :

	def csv_to_vector (self, file):

		f = open(file, 'rt')
		try:
			reader = csv.reader(f)
			for row in reader:
				for i in xrange (0,3) :
					
				print row
		finally:
			f.close()

