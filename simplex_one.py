import numpy 

class Simplex_Table():
	def __init__(self,raw_table):


		self.len = raw_table.shape

		self.matrix_B = raw_table[1:][:raw_table.shape[0]]
		self.matrix_z = raw_table[0]
		self.matrix_b = raw_table[:][-1]
		self.matrix_N = raw_table[1:] [ raw_table.shape[0] + 1 : ]

		