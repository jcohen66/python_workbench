# using property function
class Person:
    def __init__(self, name = "Someone"):
        self.__name = name   
    def setname(self, name):
        self.__name = name
    def getname(self):
        return self.__name
    def delname(self):
        del self.__name
    def __str__(self):
        return self.name
        
    name = property(getname, setname, delname)