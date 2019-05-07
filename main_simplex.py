
#main program 

import simplex_one as simplex

#1. input
x_table = []
raw_table = []
file_path = ''
file = open(file_path, 'r')

for line in file :
	raw_table.append(file.readline(line).split())

#2. Convert to readable form 
	# be aware of RHS. IT has to be only integer - NO VARIABLES 

for element in raw_table : 
	if raw_table[element] is not int or if raw_table[element] is not float : 
		raw_table.remove(element)



#3. Convert to standard form 
#4. Simplex Magic



simplex_table = simplex.Simplex_Table(raw_table) 


file.close()