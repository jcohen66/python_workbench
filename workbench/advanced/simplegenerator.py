def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code in check above generator
for value in simpleGeneratorFun():
    print(value)
    