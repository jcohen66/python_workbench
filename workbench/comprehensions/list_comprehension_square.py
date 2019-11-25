# Constructing output list using for loop 
output_list = [] 
for var in range(1, 10): 
	output_list.append(var ** 2) 
	
print("Output List using for loop:", output_list) 

# Constructing output list 
# using list comprehension 
list_using_comp = [var**2 for var in range(1, 10)] 

print("Output List using list comprehension:", 
							list_using_comp) 

