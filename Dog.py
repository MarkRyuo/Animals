from Pets import Pets 


class Dog(Pets) :
    
    # todo create constructor for dog then add the superclass constructor 
    
    def __init__(self, name, Type, breed):
        super().__init__(name, Type)
        this.breed = breed 
    
    
    # Todo call the call method in the superclass 
    
    def call(self):
        