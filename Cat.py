from Pets import Pets 



class Cat(Pets) :

    # Todo Create constructor

    def __init__(self, name, Type, breed):
        super().__init__(name, Type, breed)
    
    
    def call(self):
        super().call() # ? Call the superclass method called call
        print(f"The breed of this dog is {self.breed} \n")
        