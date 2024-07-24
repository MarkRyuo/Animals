from abc import ABC, abstractmethod 

# Todo Abstract this superclass  or the parentclass 

class Pets :
    
    
    # Todo create constructor 
    def __init__(self, name, Type ):
        self.name = name 
        self.Type = Type
    
    @abstractmethod 
    
    def call(self){
        print(f"The name of pets is {self.name}")
        print(f"The type of animal is {self.Type}")
    }
    
    