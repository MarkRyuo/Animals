from Pets import Pets 



class Cat(Pets) :

    # Todo Create constructor

    def __init__(self, name, Type, breed):
        super().__init__(name, Type)
        self.breed = breed
    
    
    def call(self):
        super().call()
        print(f"The breed of this dog is {self.breed}")