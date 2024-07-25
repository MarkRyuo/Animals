from Dog import Dog 


class Dog2(Dog) :

    # Todo create a constructor 

    def __init__(self, name, Type, breed, speak):
        super().__init__(name, Type, breed, speak)
    
    
    # todo create a method like in subclass parent 

    def call(self):
        print("\n This is Dog2 class")
        super().call()
        