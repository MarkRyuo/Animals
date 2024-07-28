from Animals import Animals 


# Todo creating a subclass for Animals 

class Dog(Animals):

    def __init__(self, Type, name, age, owner):
        super().__init__(Type, name, age, owner)
    
    
    def call(self) :
        return f"The name of this ({self.Type}) is ({self.name})" # * Solve this problem (Solved)
