from abc import ABC, abstractmethod


class Animals(ABC) :

    # Todo Name_of_animal, age_of_animal, breed_of_animal

    def __init__(self, animalName,animalAge,animalBreed) :
        self.animalName = animalName # ? Public attribute
        self.animalAge = animalAge # ? Public attribute
        self.__animalBreed = animalBreed # ? Private attribute 

    # * Encapsulation 
    def get_breed(self) :
        return self.__animalBreed # * Returning the private aatribute to access publically
    

    def get_name(self) :
        # todo create a simple logic here to check name of the animal 
        if  
    

    @abstractmethod
     
