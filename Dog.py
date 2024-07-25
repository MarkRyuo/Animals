from Pets import Pets 


class Dog(Pets) :
    
    # todo create constructor for dog then add the superclass constructor 
    
    def __init__(self, name, Type, breed, speak):
        super().__init__(name, Type, breed)
        self.speak = speak 
    
    
    # Todo call the call method in the superclass 
    
    def call(self):
        print(f"A {self.Type}, name {self.name} breed is {self.breed}")