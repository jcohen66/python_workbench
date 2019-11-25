# returning a local function
def enclosing_new():
    def local_new():
        print("I'm a new local!")
    return local_new()

print(enclosing_new())


# local and global scope
a = 'global!'
def out_new():
    b = 'enclosing!'
    def inside_new():
        c = 'locally!'
        print(a, b, c)
    inside_new()
print(out_new())