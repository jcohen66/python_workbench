# new local function
def new_function():
    def new_local_function():
        print("My name is local function!")
    print(new_local_function())
    print("Not a local function")
    
print(new_function())

def remove_first(new_list):
    def get_first(first):
        return first[0]
    new_list.remove(get_first(new_list))
    return new_list

print(remove_first([2, 4, 6, 8]))
print(get_first([2, 4, 6, 8]))