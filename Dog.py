from Animals import Animals 


class Dog(Animals) :


    # Todo create constructor for Dog ang import superclass 

    def __init__(self, animalName, animalAge, animalBreed) :
        super().__init__(animalName, animalAge, animalBreed) 
    

    def display(self):
        return super().display()