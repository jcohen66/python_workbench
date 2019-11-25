# build new point generator
def new_point():
    n = 1
    print('first of all!!!')
    
    # yield inside generator
    yield n
    
    n += 1
    print("It's displayed second!")
    yield n
    
    n += 1
    print("It's displayed third!")
    yield n
    
    
x = new_point()

# iterate thru with next
print(next(x))
print(next(x))
print(next(x))

# after completion, StopIteration is raised.
print(next(x))


# loop thru generator
for point in new_point():
    print(point)
