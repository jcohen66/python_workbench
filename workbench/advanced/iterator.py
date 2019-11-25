# creating a list
new_list = [1, 2, 3, 7, 9]

# using iter()
new_iter = iter(new_list)

# print 1
print(next(new_iter))

# print 2
print(next(new_iter))

# print 3
print(new_iter.__next__())

# print 7
print(new_iter.__next__())

# print 9
print(new_iter.__next__())

# looping thru new_list
for element in new_list:
    print(element)
    
# build an iterator
class NewNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
newclass = NewNumbers()
newiter = iter(newclass)

#print the iteration
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))
print(next(newiter))



    
    