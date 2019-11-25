# take many args
def new_args(**kwargs):
    print(kwargs)
    
print(new_args(first = 'new name'))
print(new_args(first = 'new name', second = 'second name'))
print(new_args())

def displaying_args(**kwargs):
    for key, value in kwargs.items():
        print('{0}: {1}'.format(key, value))
        
        
displaying_args(first= "new name", second="second name")