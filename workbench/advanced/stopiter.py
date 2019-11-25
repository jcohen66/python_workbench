# build iterator and stop it
class NewNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 15:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
        
newclass = NewNumbers()
newiter = iter(newclass)
    
# loop thru newiter
for x in newiter:
    print(x)
    
    