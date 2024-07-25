from Pets import Pets 


class Dog(Pets) :
    
    # todo create constructor for dog then add the superclass constructor 
    
    def __init__(self, name, Type, breed, speak):
        super().__init__(name, Type, breed)
        self.speak = speak 
    
    
    # Todo call the call method in the superclass 
    
    def call(self):
        print("This is a Dog class")
        print(f"A {self.Type}, name {self.name} breed is {self.breed}")



# * Dog is subclass of Pets a superclass but this point the Dog has a subclass name Dog2 
# * A subclass have a subclass  