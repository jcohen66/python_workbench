# Adding arguments in a function
def new_adding(*args):
    result = 0
    for x in args:
        result += x
    return result

print(new_adding(1, 2, 3, 4, 5))
print(new_adding(10, 20, 30))
print(new_adding())
print(new_adding(10))

