# using a closure
def new_out():
    x = 10
    def new_in(y = 5):
        return (x + y)
    return new_in

a = new_out()

print(a())

# closure example for mult by number n
def new_multi(num):
    def num_multi(n):
        return num * n
    return num_multi

five_multi = new_multi(5)
print(five_multi(3))

eight_multi = new_multi(8)
print(eight_multi(8))
