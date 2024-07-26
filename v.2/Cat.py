from Pets import Pets 



class Cat(Pets) :

    # Todo Create constructor

    def __init__(self, name, Type, breed):
        super().__init__(name, Type, breed)
    
    
    def call(self):
        print("\n This is a Cat class ")
        print(f"A {self.Type}, name {self.name} breed is {self.breed}")
        