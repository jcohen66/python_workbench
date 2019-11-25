# pass speaking function into new_capital decorator
def new_capital(func):
    def new_uppercase():
        result = func() 
        return result.upper()
    return new_uppercase

@new_capital
def speaking():
    return "Hi from the other side!"

print(speaking())


