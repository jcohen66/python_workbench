# display the power
new_list = [2, 4, 6, 8]

x = (a**2 for a in new_list)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#print(next(x))  # StopIteration

y = (a**2 for a in new_list)
print(sum(y))

z = (a**2 for a in new_list)
print(max(z))