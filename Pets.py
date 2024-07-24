from abc import ABC, abstractmethod 

# Todo Abstract this superclass  or the parentclass 

class Pets(ABC) :
    
    
    # Todo create constructor 
    def __init__(self, name, Type ):
        self.name = name 
        self.Type = Type
    
    @abstractmethod 
    def call(self) : 
        print(f"My {self.Type} is {self.name}")
    
    
    
    
    