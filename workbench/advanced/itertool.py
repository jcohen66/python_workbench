from itertools import product
for i in product([1,2,3],[4.5,6]):
    print(i) 
    
for i in product('AB', 'CD', 'EF'):
    print(i) 
    
for i in product('AB', 'CD', repeat=2):
    print(i)