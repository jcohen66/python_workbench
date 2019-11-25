state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 

output_dict = {} 

# Using loop for constructing output dictionary 
for (key, value) in zip(state, capital): 
	output_dict[key] = value 

print("Output Dictionary using for loop:", 
							output_dict) 

# Using Dictionary comprehensions 
# for constructing output dictionary 
  
state = ['Gujarat', 'Maharashtra', 'Rajasthan'] 
capital = ['Gandhinagar', 'Mumbai', 'Jaipur'] 
  
dict_using_comp = {key:value for (key, value) in zip(state, capital)} 
  
print("Output Dictionary using dictionary comprehensions:",  
                                           dict_using_comp) 