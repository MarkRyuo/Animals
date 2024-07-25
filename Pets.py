from abc import ABC, abstractmethod 

# Todo Abstract this superclass  or the parentclass 

class Pets(ABC) :
    
    
    # Todo create constructor 
    def __init__(self, name, Type, breed ):
        self.name = name 
        self.Type = Type
        self.breed = breed

    @abstractmethod 
    def call(self) : 