from Animals import Animals 


# Todo creating a subclass for Animals 

class Dog(Animals):

    def __init__(self, Type, name, age):
        super().__init__(Type, name, age)
    

    def call(self) :
        print(f"The name of this {self.Type} is {self.name}, age of {}")
