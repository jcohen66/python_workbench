input_list = [1, 2, 3, 4, 5, 6, 7] 

output_dict = {} 

# Using loop for constructing output dictionary 
for var in input_list: 
	if var % 2 != 0: 
		output_dict[var] = var**3

print("Output Dictionary using for loop:", 
							output_dict ) 

# Using Dictionary comprehensions 
# for constructing output dictionary 

input_list = [1,2,3,4,5,6,7] 

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0} 

print("Output Dictionary using dictionary comprehensions:", 
										dict_using_comp) 

