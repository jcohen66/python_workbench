# strings are iterable objects so * will unpack it and place
# all individual values in a.
a = [*"RealPython"]
print(a)

# does the same thing

# The comma after the a does the trick. When you use the unpacking 
# operator with variable assignment, Python requires that your resulting 
# variable is either a list or a tuple. With the trailing comma, you have 
# actually defined a tuple with just one named variable a.
*b, = "RealPython"
print(b)

