from typing import override
from Animals import Animals 


# Todo creating a subclass for Animals 

class Dog(Animals):

    def __init__(self, Type, name, age):
        super().__init__(Type, name, age)
    
    
    # * get the get_age method in superclass  
    def get_age(self):
        return self.__age
