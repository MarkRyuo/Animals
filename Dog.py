from Pets import Pets 


class Dog(Pets) :
    
    # todo create constructor for dog then add the superclass constructor 
    
    def __init__(self, name, Type, breed):
        super().__init__(name, Type)
        self.breed = breed 
    
    
    # Todo call the call method in the superclass 
    
    def call(self):
        super().call
        print(f"The breed of this dog is {self.breed}")