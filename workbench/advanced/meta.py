class NewMetaClass(type):
    __metaclass__ = type
    print("I'm a new metaclass")
    
class NewDemoClass:
    __metaclass__ = NewMetaClass
    print("Hi I'm a demo")
    
obj = NewDemoClass()
print(obj.__metaclass__)
print(NewMetaClass.__metaclass__)

